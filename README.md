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
### 📅 Latest snapshot — 2026-10-11

> *"You only live once, but if you do it right, once is enough."* — **Mae West**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $82,934 | +0.24% |
| Ethereum | $2,499.52 | +0.3% |
| Solana | $109.48 | +0.01% |

**🔭 NASA:** [NASA Science](https://science.nasa.gov/wp-content/themes/nasa-child/assets/images/nasa-logo@2x.png)

**🚗 Car news:** [Alfa Romeo's New Sports Car Teases A Four-Seat Layout: Video](https://www.motor1.com/news/811404/alfa-romeo-sports-car-interior-teaser/)

**📜 On this day, 944:** Caliph al-Muttaqi is blinded and deposed by the Turkish general Tuzun. — [Al-Muttaqi](https://en.wikipedia.org/wiki/Al-Muttaqi)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 12 followers

<!-- LATEST:END -->
