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
### 📅 Latest snapshot — 2026-10-12

> *"Those who know, do. Those that understand, teach."* — **Aristotle**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $83,349 | +0.44% |
| Ethereum | $2,544.89 | +1.83% |
| Solana | $111.22 | +1.7% |

**🚗 Car news:** [Avatr T09 Debuts With Six Seats And 1,000-HP Hybrid System](https://www.motor1.com/news/811595/avatr-t09-hybrid-suv-debuts/)

**📜 On this day, -539:** The army of Cyrus the Great of Persia conquer Babylon, ending the Babylonian empire. (Julian calendar) — [Cyrus the Great](https://en.wikipedia.org/wiki/Cyrus_the_Great)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 12 followers

<!-- LATEST:END -->
