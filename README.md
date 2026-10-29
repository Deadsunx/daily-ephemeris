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
### 📅 Latest snapshot — 2026-10-29

> *"The more reasons you have for achieving your goal, the more determined you will become."* — **Brian Tracy**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $80,181 | -1.56% |
| Ethereum | $2,321.17 | -1.95% |
| Solana | $100.25 | -2.74% |

**🚗 Car news:** [Winter Storm Warning Issued for Up to 15 Inches of Snow Through Friday](https://www.autoblog.com/news/winter-storm-warning-issued-for-up-to-15-inches-of-snow-through-friday)

**📜 On this day, 312:** Constantine the Great enters Rome after his victory at the Battle of the Milvian Bridge, stages a grand adventus in the city, and is met with popular jubilation. Maxentius' body is fished out of the Tiber and beheaded. — [Constantine the Great](https://en.wikipedia.org/wiki/Constantine_the_Great)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 11 followers

<!-- LATEST:END -->
