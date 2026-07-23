#!/usr/bin/env python3
"""Daily data archive.

Fetches six free sources (no API key required):
  1. Crypto prices (+ 30d) -> CoinGecko
  2. Quote of the day      -> ZenQuotes
  3. NASA picture of day   -> NASA APOD (public DEMO_KEY)
  4. Car news headline     -> a car-news RSS feed
  5. On this day (history) -> Wikipedia REST
  6. GitHub profile stats  -> GitHub public API

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
import time
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

# Whose public GitHub stats to show. Override with env var GITHUB_USER.
GITHUB_USER = os.environ.get("GITHUB_USER", "Deadsunx")

# Coins tracked, and how many days of history to keep for the sparklines.
COINS = ("bitcoin", "ethereum", "solana")
SPARK_DAYS = 30

# Tried in order until one parses; first working feed wins.
CAR_FEEDS = [
    "https://www.autoblog.com/rss.xml",
    "https://www.motor1.com/rss/news/all/",
    "https://www.caranddriver.com/rss/all.xml/",
]

HEADERS = {"User-Agent": "daily-data-archive/1.0 (+github actions)"}


def _get(url: str, timeout: int = 20, retries: int = 3) -> bytes:
    last_err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except Exception as err:
            last_err = err
            if attempt < retries - 1:
                time.sleep(2 ** attempt)  # 1s, 2s backoff
    raise last_err


def _get_json(url: str):
    return json.loads(_get(url))


def _spark(coin: str) -> list:
    """Return ~30 daily USD prices for a coin, for the web page's sparkline."""
    try:
        url = (
            f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"
            f"?vs_currency=usd&days={SPARK_DAYS}&interval=daily"
        )
        prices = _get_json(url).get("prices", [])
        return [round(p[1], 2) for p in prices]
    except Exception:
        return []  # sparkline is a nice-to-have, never fail the whole reading


def fetch_crypto() -> dict:
    url = (
        "https://api.coingecko.com/api/v3/simple/price"
        f"?ids={','.join(COINS)}"
        "&vs_currencies=usd&include_24hr_change=true&include_market_cap=true"
    )
    data = _get_json(url)
    out = {}
    for coin in COINS:
        if coin in data:
            out[coin] = {
                "usd": data[coin].get("usd"),
                "usd_24h_change": round(data[coin].get("usd_24h_change", 0), 2),
                "usd_market_cap": data[coin].get("usd_market_cap"),
                "spark": _spark(coin),
            }
    return out


def fetch_onthisday() -> dict:
    """A notable historical event on today's month/day (Wikipedia, keyless)."""
    now = datetime.now(timezone.utc)
    url = (
        "https://en.wikipedia.org/api/rest_v1/feed/onthisday/events/"
        f"{now:%m}/{now:%d}"
    )
    events = _get_json(url).get("events", [])
    if not events:
        raise RuntimeError("no events returned")
    # Prefer an older, well-formed event with a linked page.
    ev = max(events, key=lambda e: (bool(e.get("pages")), -int(e.get("year", 0))))
    page = (ev.get("pages") or [{}])[0]
    return {
        "year": ev.get("year"),
        "text": (ev.get("text") or "").strip(),
        "title": page.get("titles", {}).get("normalized") or page.get("title"),
        "url": page.get("content_urls", {}).get("desktop", {}).get("page"),
    }


def fetch_github() -> dict:
    """Public profile stats for GITHUB_USER — ties the archive to the streak."""
    data = _get_json(f"https://api.github.com/users/{GITHUB_USER}")
    return {
        "login": data.get("login"),
        "name": data.get("name"),
        "public_repos": data.get("public_repos"),
        "followers": data.get("followers"),
        "following": data.get("following"),
        "created_at": data.get("created_at"),
        "html_url": data.get("html_url"),
        "avatar_url": data.get("avatar_url"),
    }


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
    "onthisday": fetch_onthisday,
    "github": fetch_github,
}

# Which readings count as "captured" for the ledger/calendar.
READINGS = tuple(SOURCES.keys())


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

    # latest.json: what the web page loads first.
    (ARCHIVE / "latest.json").write_text(
        json.dumps(snapshot, indent=2), encoding="utf-8"
    )


def write_index() -> None:
    """Rebuild archive/index.json: one entry per archived day, oldest first.

    Each entry records the date and which readings succeeded that day, so the
    web page's ledger can show at a glance what was captured.
    """
    entries = []
    for path in sorted(ARCHIVE.glob("*.json")):
        if path.stem in ("latest", "index"):
            continue
        try:
            day = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        ok = [
            name
            for name in READINGS
            if isinstance(day.get(name), dict) and "error" not in day[name]
        ]
        entries.append({"date": day.get("date", path.stem), "captured": ok})
    (ARCHIVE / "index.json").write_text(
        json.dumps(entries, indent=2), encoding="utf-8"
    )
    print(f"wrote index with {len(entries)} entries")


CSV_HEADER = ["date", "coin", "usd", "usd_24h_change", "usd_market_cap"]


def append_crypto_csv(snapshot: dict) -> None:
    """Record one row per (date, coin). Re-running a day updates it in place,
    so multiple runs (e.g. the backup cron) never duplicate rows."""
    crypto = snapshot.get("crypto")
    if not crypto or "error" in crypto:
        return
    DATA.mkdir(exist_ok=True)
    path = DATA / "crypto.csv"

    # Load existing rows, keyed by (date, coin) so today's overwrites cleanly.
    rows: dict[tuple, list] = {}
    if path.exists():
        with path.open(newline="", encoding="utf-8") as f:
            for i, row in enumerate(csv.reader(f)):
                if i == 0 or len(row) < 2:
                    continue  # skip header / blanks
                rows[(row[0], row[1])] = row

    for coin, vals in crypto.items():
        rows[(snapshot["date"], coin)] = [
            snapshot["date"], coin,
            vals.get("usd"), vals.get("usd_24h_change"), vals.get("usd_market_cap"),
        ]

    # Sort by date, then by tracked-coin order.
    order = {c: i for i, c in enumerate(COINS)}
    ordered = sorted(rows.values(), key=lambda r: (r[0], order.get(r[1], 99)))
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(CSV_HEADER)
        w.writerows(ordered)


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

    otd = snapshot.get("onthisday", {})
    if otd and "error" not in otd:
        link = f"[{otd['title']}]({otd['url']})" if otd.get("url") else otd.get("text", "")
        lines.append(f"**📜 On this day, {otd.get('year')}:** {otd.get('text')} — {link}")
        lines.append("")

    gh = snapshot.get("github", {})
    if gh and "error" not in gh:
        lines.append(
            f"**🐙 GitHub [@{gh['login']}]({gh['html_url']}):** "
            f"{gh['public_repos']} repos · {gh['followers']} followers"
        )
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
    write_index()
    append_crypto_csv(snapshot)
    update_readme(snapshot)
    print("done")


if __name__ == "__main__":
    main()
