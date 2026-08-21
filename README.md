# Daily Data Archive 🌍

A small project that builds a **growing dataset** by fetching four free sources
every single day and archiving them — all automatically via a scheduled
[GitHub Actions](https://docs.github.com/actions) workflow.

Because the automation runs on **GitHub's servers**, the daily commit happens
whether my laptop is on or off.

**🌐 Live page → https://deadsunx.github.io/daily-ephemeris/**
_(the "Ephemeris" — a daily record of sky, market, word & road)_

## What it collects each day

| # | Source | Provider |
| - | ------ | -------- |
| 1 | Crypto prices (BTC / ETH / SOL) | CoinGecko |
| 2 | Quote of the day | ZenQuotes |
| 3 | Astronomy Picture of the Day | NASA APOD |
| 4 | Top car-news headline | Car-news RSS feed |

## How it works

1. `.github/workflows/daily.yml` runs [`daily_update.py`](daily_update.py) once a day.
2. The script saves a dated snapshot to [`archive/`](archive), appends crypto
   prices to [`data/crypto.csv`](data/crypto.csv), and refreshes the block below.
3. It commits and pushes **as me**, so it counts toward my contribution graph.

## Run it locally

```bash
python daily_update.py
```

Only the Python standard library is used — nothing to install.

<!-- LATEST:START -->
### 📅 Latest snapshot — 2026-08-21

> *"Listen to the secret sound, the real sound, which is inside you."* — **Kabir**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $77,262 | +6.8% |
| Ethereum | $2,399.44 | +3.28% |
| Solana | $91.39 | +5.02% |

**🔭 NASA:** [Time-Lapse of the Star S301 Orbiting the Black Hole in the Center of the Galaxy](https://apod.nasa.gov/apod/image/2608/eso2612b.mp4)

**🚗 Car news:** [Brabus Built Its Own Million-Dollar GT, and It Won’t Be the Last](https://www.autoblog.com/news/brabus-built-its-own-million-dollar-gt-and-it-wont-be-the-last)

**📜 On this day, 959:** Eraclus becomes the 25th bishop of Liège. — [Eraclus](https://en.wikipedia.org/wiki/Eraclus)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 10 repos · 8 followers

<!-- LATEST:END -->
