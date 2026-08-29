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
### 📅 Latest snapshot — 2026-08-29

> *"Don't put off living to next week, next month, next year or next decade. The only time you're ever living is in this moment."* — **Celestine Chua**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $77,911 | -3.12% |
| Ethereum | $2,445.31 | -2.69% |
| Solana | $104.44 | -4.76% |

**🔭 NASA:** [The Sky Turns Above Paranal](https://apod.nasa.gov/apod/image/2608/TheSkyTurnsAboveParanal_1024.jpg)

**🚗 Car news:** [Acura Said It Wouldn't Build A Sports Car. Now The Door Is Open](https://www.motor1.com/news/806427/acura-nexera-production-version-possible/)

**📜 On this day, 708:** Copper coins are minted in Japan for the first time (Traditional Japanese date: August 10, 708). — [Wadōkaichin](https://en.wikipedia.org/wiki/Wad%C5%8Dkaichin)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 10 repos · 9 followers

<!-- LATEST:END -->
