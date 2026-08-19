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
### 📅 Latest snapshot — 2026-08-19

> *"Why change? Everyone has his own style. When you have found it, you should stick to it."* — **Audrey Hepburn**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $68,757 | +6.32% |
| Ethereum | $2,097.57 | +9.65% |
| Solana | $81.91 | +6.61% |

**🔭 NASA:** [The Case of the Mysterious Maybe Meteor](https://apod.nasa.gov/apod/image/2608/perseids_eclipse_mystery.mp4)

**🚗 Car news:** [Lamborghini's Hybrid Future Is Taking Shape, And One Country Could Have A Bigger Role](https://www.motor1.com/news/805470/lamborghini-hybrid-strategy-puts-canada/)

**📜 On this day, -295:** The first temple to Venus, the Roman goddess of love, beauty and fertility, is dedicated by Quintus Fabius Maximus Gurges during the Third Samnite War. — [Venus (mythology)](https://en.wikipedia.org/wiki/Venus_(mythology))

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 10 repos · 6 followers

<!-- LATEST:END -->
