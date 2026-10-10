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
### 📅 Latest snapshot — 2026-10-10

> *"Ability is a poor man's wealth."* — **John Wooden**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $82,761 | +0.2% |
| Ethereum | $2,492.8 | -0.18% |
| Solana | $109.59 | -0.57% |

**🚗 Car news:** [Alfa Romeo's New Sports Car Teases A Four-Seat Layout: Video](https://www.motor1.com/news/811404/alfa-romeo-sports-car-interior-teaser/)

**📜 On this day, 19:** The Roman general Germanicus dies near Antioch. He was convinced that the mysterious illness that ended in his death was a result of poisoning by the Syrian governor Gnaeus Calpurnius Piso, whom he had ordered to leave the province. — [10s](https://en.wikipedia.org/wiki/10s)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 12 followers

<!-- LATEST:END -->
