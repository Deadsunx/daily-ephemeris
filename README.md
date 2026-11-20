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
### 📅 Latest snapshot — 2026-11-20

> *"Never waste a minute of your precious life thinking about people you don't like."* — **Celestine Chua**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $61,504 | -3.48% |
| Ethereum | $1,736.89 | -3.66% |
| Solana | $71.13 | -4.76% |

**🚗 Car news:** [Geely Launches Lynk & Co 07 GT Off A Cliff To Prove Its Safety](https://www.motor1.com/news/816232/lynk-co-07-gt-safety/)

**📜 On this day, 284:** Diocletian is chosen as Roman emperor. — [Diocletian](https://en.wikipedia.org/wiki/Diocletian)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 8 followers

<!-- LATEST:END -->
