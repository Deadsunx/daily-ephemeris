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
### 📅 Latest snapshot — 2026-10-25

> *"The wiser you get, the less you care to look like a fool."* — **Maxime Lagace**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $80,625 | +0.46% |
| Ethereum | $2,353.37 | +1.01% |
| Solana | $101.88 | +0.94% |

**🚗 Car news:** [Every Detail Packed Into The Bentley Torcal First Edition](https://www.motor1.com/news/812983/bentley-torcal-special-edition-details/)

**📜 On this day, 473:** Emperor Leo I acclaims his grandson Leo II as Caesar of the East Roman Empire. — [Leo I (emperor)](https://en.wikipedia.org/wiki/Leo_I_(emperor))

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 10 followers

<!-- LATEST:END -->
