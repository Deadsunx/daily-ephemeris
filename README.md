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
### 📅 Latest snapshot — 2026-08-13

> *"Keep your face to the sunshine and you cannot see the shadows."* — **Helen Keller**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $63,149 | -0.47% |
| Ethereum | $1,874.45 | -0.8% |
| Solana | $75.55 | -0.06% |

**🔭 NASA:** [Total Solar Eclipse Over Spain](https://apod.nasa.gov/apod/image/2608/total_solar_eclipse_900.jpg)

**🚗 Car news:** [Ferrari Files 'LC67' Trademark. Is Another Special Model Coming?](https://www.motor1.com/news/804820/ferrari-lc67-trademark-filing-adds/)

**📜 On this day, -29:** Octavian holds the first of three consecutive triumphs in Rome to celebrate the victory over the Dalmatian tribes. — [Augustus](https://en.wikipedia.org/wiki/Augustus)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 9 repos · 4 followers

<!-- LATEST:END -->
