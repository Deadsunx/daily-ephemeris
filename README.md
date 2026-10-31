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
### 📅 Latest snapshot — 2026-10-31

> *"When you believe in a thing, believe in it all the way, implicitly and unquestionable."* — **Walt Disney**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $77,358 | -0.15% |
| Ethereum | $2,241.53 | +0.8% |
| Solana | $95.39 | -1.05% |

**🚗 Car news:** [Winter Weather Advisory: Up to 10 Inches of Snow and 35 MPH Gusts Through Sunday](https://www.autoblog.com/news/winter-weather-advisory-up-to-10-inches-of-snow-and-35-mph-gusts-through-sunday)

**📜 On this day, 475:** Romulus Augustulus is proclaimed Western Roman Emperor. — [Romulus Augustulus](https://en.wikipedia.org/wiki/Romulus_Augustulus)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 11 followers

<!-- LATEST:END -->
