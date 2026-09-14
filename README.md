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
### 📅 Latest snapshot — 2026-09-14

> *"If you spend too much time thinking about a thing, you'll never get it done."* — **Bruce Lee**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $79,024 | +2.31% |
| Ethereum | $2,543.55 | +1.5% |
| Solana | $103.36 | +2.3% |

**🔭 NASA:** [Where Your Elements Came From](https://apod.nasa.gov/apod/image/2609/ElementOrigins2_svs_1080.jpg)

**🚗 Car news:** [Corvette Grand Sport Buyers Clearly Have A Favorite Color](https://www.motor1.com/news/808228/2027-corvette-grand-sport-production/)

**📜 On this day, 81:** Domitian became Emperor of the Roman Empire upon the death of his brother Titus. — [AD 81](https://en.wikipedia.org/wiki/AD_81)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
