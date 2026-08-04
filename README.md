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
### 📅 Latest snapshot — 2026-08-04

> *"Love never keeps a man from pursuing his destiny."* — **Paulo Coelho**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $64,069 | +0.35% |
| Ethereum | $1,874.9 | +0.36% |
| Solana | $74.03 | +0.49% |

**🔭 NASA:** [Curious Cometary Knots in the Helix Nebula](https://apod.nasa.gov/apod/image/2608/HelixKnots_JWST_960.jpg)

**🚗 Car news:** [Watch A Honda Prelude Tackle The Infamous Moose Test](https://www.motor1.com/news/803752/honda-prelude-passes-moose-test/)

**📜 On this day, -70:** The trial against Gaius Verres for corruption is opened, with Marcus Tullius Cicero as prosecutor and renowned orator Quintus Hortensius as defending lawyer. — [Gaius Verres](https://en.wikipedia.org/wiki/Gaius_Verres)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 7 repos · 0 followers

<!-- LATEST:END -->
