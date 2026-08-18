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
### 📅 Latest snapshot — 2026-08-18

> *"No one can compete with you on being you. Most of life is a search for who and what needs you the most."* — **Naval Ravikant**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $64,691 | +1.01% |
| Ethereum | $1,914.14 | +0.38% |
| Solana | $76.89 | +1.26% |

**🔭 NASA:** [Perseids from Perseus](https://apod.nasa.gov/apod/image/2608/Perseids_karuk_960.jpg)

**🚗 Car news:** [McLaren's Manual Supercar Isn't A Preview Of The Future](https://www.motor1.com/news/805359/mclaren-manual-supercar-wont-influence-future-cars/)

**📜 On this day, 684:** Battle of Marj Rahit: Umayyad partisans defeat the supporters of Ibn al-Zubayr and cement Umayyad control of Syria. — [Battle of Marj Rahit (684)](https://en.wikipedia.org/wiki/Battle_of_Marj_Rahit_(684))

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 10 repos · 6 followers

<!-- LATEST:END -->
