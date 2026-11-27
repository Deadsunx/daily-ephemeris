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
### 📅 Latest snapshot — 2026-11-27

> *"It takes half your life before you discover life is a do-it-yourself project."* — **Napoleon Hill**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $59,861 | -1.0% |
| Ethereum | $1,660.47 | -1.51% |
| Solana | $71.51 | +0.79% |

**🚗 Car news:** [Michael Schumacher’s Porsche Carrera GT Is Going to Auction With A Remarkable Paper Trail](https://www.motor1.com/news/817030/michael-schumacher-porsche-carrera-gt/)

**📜 On this day, 25:** Luoyang is declared capital of the Eastern Han dynasty by Emperor Guangwu of Han. — [20s](https://en.wikipedia.org/wiki/20s)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 7 followers

<!-- LATEST:END -->
