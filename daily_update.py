#!/usr/bin/env python3
"""Daily data archive.

Fetches four free sources (no API key required for most):
  1. Crypto prices        -> CoinGecko
  2. Quote of the day      -> ZenQuotes
  3. NASA picture of day   -> NASA APOD (public DEMO_KEY)
  4. Car news headline     -> a car-news RSS feed

Writes a dated snapshot to archive/YYYY-MM-DD.json, appends crypto prices to
data/crypto.csv, and refreshes the "Latest snapshot" block in README.md.

Uses only the Python standard library, so the GitHub Actions workflow needs no
`pip install`. Every source is wrapped in try/except: if one is down, the rest
still succeed and the daily commit still happens.
"""

from __future__ import annotations

import csv
import json
import os
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent
ARCHIVE = ROOT / "archive"
DATA = ROOT / "data"
README = ROOT / "README.md"

# NASA offers a public DEMO_KEY; override via env var NASA_API_KEY if you get one.
NASA_KEY = os.environ.get("NASA_API_KEY", "DEMO_KEY")

# Tried in order until one parses; first working feed wins.
CAR_FEEDS = [
    "https://www.autoblog.com/rss.xml",
    "https://www.motor1.com/rss/news/all/",
    "https://www.caranddriver.com/rss/all.xml/",
]

HEADERS = {"User-Agent": "daily-data-archive/1.0 (+github actions)"}


def _get(url: str, timeout: int = 20) -> bytes:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def _get_json(url: str):
    return json.loads(_get(url))


def fetch_crypto() -> dict:
    url = (
        "https://api.coingecko.com/api/v3/simple/price"
        "?ids=bitcoin,ethereum,solana"
        "&vs_currencies=usd&include_24hr_change=true&include_market_cap=true"
    )
    data = _get_json(url)
    out = {}
    for coin in ("bitcoin", "ethereum", "solana"):
        if coin in data:
            out[coin] = {
                "usd": data[coin].get("usd"),
                "usd_24h_change": round(data[coin].get("usd_24h_change", 0), 2),
                "usd_market_cap": data[coin].get("usd_market_cap"),
            }
    return out


def fetch_quote() -> dict:
    data = _get_json("https://zenquotes.io/api/today")
    item = data[0]
    return {"text": item.get("q", "").strip(), "author": item.get("a", "").strip()}


def fetch_nasa() -> dict:
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_KEY}"
    data = _get_json(url)
    return {
        "title": data.get("title"),
        "explanation": data.get("explanation"),
        "url": data.get("url"),
        "media_type": data.get("media_type"),
    }


def fetch_car_news() -> dict:
    last_err = None
    for feed in CAR_FEEDS:
        try:
            root = ET.fromstring(_get(feed))
            item = root.find(".//channel/item")
            if item is None:
                item = root.find(".//{http://www.w3.org/2005/Atom}entry")
            if item is None:
                continue
            title = item.findtext("title") or item.findtext(
                "{http://www.w3.org/2005/Atom}title"
            )
            link = item.findtext("link")
            if not link:  # Atom stores link in an attribute
                link_el = item.find("{http://www.w3.org/2005/Atom}link")
                link = link_el.get("href") if link_el is not None else None
            return {
                "headline": (title or "").strip(),
                "url": (link or "").strip(),
                "source": feed,
            }
        except Exception as err:  # try the next feed
            last_err = err
            continue
    raise RuntimeError(f"all car feeds failed: {last_err}")


SOURCES = {
    "crypto": fetch_crypto,
    "quote": fetch_quote,
    "nasa": fetch_nasa,
    "car_news": fetch_car_news,
}


def collect() -> dict:
    now = datetime.now(timezone.utc)
    snapshot = {"date": now.strftime("%Y-%m-%d"), "fetched_at": now.isoformat()}
    for name, fn in SOURCES.items():
        try:
            snapshot[name] = fn()
            print(f"[ok]   {name}")
        except Exception as err:
            snapshot[name] = {"error": str(err)}
            print(f"[fail] {name}: {err}")
    return snapshot


def write_archive(snapshot: dict) -> None:
    ARCHIVE.mkdir(exist_ok=True)
    path = ARCHIVE / f"{snapshot['date']}.json"
    path.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")
    print(f"wrote {path}")


def append_crypto_csv(snapshot: dict) -> None:
    crypto = snapshot.get("crypto")
    if not crypto or "error" in crypto:
        return
    DATA.mkdir(exist_ok=True)
    path = DATA / "crypto.csv"
    new = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["date", "coin", "usd", "usd_24h_change", "usd_market_cap"])
        for coin, vals in crypto.items():
            w.writerow(
                [
                    snapshot["date"],
                    coin,
                    vals.get("usd"),
                    vals.get("usd_24h_change"),
                    vals.get("usd_market_cap"),
                ]
            )


def update_readme(snapshot: dict) -> None:
    if not README.exists():
        return
    lines = ["<!-- LATEST:START -->", f"### 📅 Latest snapshot — {snapshot['date']}", ""]

    q = snapshot.get("quote", {})
    if q and "error" not in q:
        lines.append(f"> *\"{q['text']}\"* — **{q['author']}**")
        lines.append("")

    c = snapshot.get("crypto", {})
    if c and "error" not in c:
        lines.append("**Crypto (USD)**")
        lines.append("")
        lines.append("| Coin | Price | 24h |")
        lines.append("| --- | --- | --- |")
        for coin, v in c.items():
            lines.append(f"| {coin.title()} | ${v['usd']:,} | {v['usd_24h_change']:+}% |")
        lines.append("")

    n = snapshot.get("nasa", {})
    if n and "error" not in n:
        lines.append(f"**🔭 NASA:** [{n['title']}]({n['url']})")
        lines.append("")

    car = snapshot.get("car_news", {})
    if car and "error" not in car:
        lines.append(f"**🚗 Car news:** [{car['headline']}]({car['url']})")
        lines.append("")

    lines.append("<!-- LATEST:END -->")
    block = "\n".join(lines)

    text = README.read_text(encoding="utf-8")
    start, end = "<!-- LATEST:START -->", "<!-- LATEST:END -->"
    if start in text and end in text:
        pre = text[: text.index(start)]
        post = text[text.index(end) + len(end) :]
        text = pre + block + post
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    README.write_text(text, encoding="utf-8")


def main() -> None:
    snapshot = collect()
    write_archive(snapshot)
    append_crypto_csv(snapshot)
    update_readme(snapshot)
    print("done")


if __name__ == "__main__":
    main()
