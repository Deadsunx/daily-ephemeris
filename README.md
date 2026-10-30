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
### 📅 Latest snapshot — 2026-10-30

> *"Distant water does not put out a nearby fire."* — **Chinese Proverb**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $77,563 | -3.25% |
| Ethereum | $2,239.86 | -3.55% |
| Solana | $97.02 | -3.32% |

**🔭 NASA:** [NASA Science](https://science.nasa.gov/wp-content/themes/nasa-child/assets/images/nasa-logo@2x.png)

**🚗 Car news:** [Winter Weather Advisory Issued for Up to 12 Inches of Snow and 50 MPH Gusts This Weekend](https://www.autoblog.com/news/winter-weather-advisory-issued-for-up-to-12-inches-of-snow-and-50-mph-gusts-this-weekend)

**📜 On this day, 130:** Emperor Hadrian establishes the city of Antinoöpolis on the Nile in honour of his companion Antinous, creating a new Hellenizing foundation in Roman Egypt. — [AD 130](https://en.wikipedia.org/wiki/AD_130)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 11 followers

<!-- LATEST:END -->
