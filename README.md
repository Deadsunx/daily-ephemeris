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
### 📅 Latest snapshot — 2026-10-03

> *"We are born from a quiet sleep, and we die to a calm awakening"* — **Zhuangzi**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $84,931 | +0.79% |
| Ethereum | $2,683.89 | +0.7% |
| Solana | $119.88 | +1.51% |

**🚗 Car news:** [Stellantis CEO Sees A 'Huge Opportunity' For Cheap Cars](https://www.motor1.com/news/810664/stellantis-ceo-cheap-cars-opportunity/)

**📜 On this day, -2457:** Gaecheonjeol, Hwanung (환웅) purportedly descended from heaven. South Korea's National Foundation Day. — [National Foundation Day (Korea)](https://en.wikipedia.org/wiki/National_Foundation_Day_(Korea))

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 11 followers

<!-- LATEST:END -->
