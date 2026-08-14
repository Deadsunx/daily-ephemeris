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
### 📅 Latest snapshot — 2026-08-14

> *"Extraordinary results happen only when you give the best you have to become the best you can be at your most important work."* — **Gary Keller**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $63,285 | -0.95% |
| Ethereum | $1,880.62 | -0.85% |
| Solana | $75.81 | -0.6% |

**🔭 NASA:** [Total Solar Eclipse from Greenland](https://apod.nasa.gov/apod/image/2608/TSE2026DR_Madhaven1024.jpeg)

**🚗 Car news:** [Mercedes Won't Stop Building V8s, But A New C63 May Not Happen](https://www.motor1.com/news/804864/mercedes-benz-v8-engine-producion-decaade-c63/)

**📜 On this day, -74:** A group of officials, led by the Western Han minister Huo Guang, present articles of impeachment against the new emperor, Liu He, to the imperial regent, Empress Dowager Shangguan. — [Han dynasty](https://en.wikipedia.org/wiki/Han_dynasty)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 9 repos · 4 followers

<!-- LATEST:END -->
