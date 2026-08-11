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
### 📅 Latest snapshot — 2026-08-11

> *"Still your waters."* — **Josh Waitzkin**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $63,466 | -0.56% |
| Ethereum | $1,863.05 | -0.32% |
| Solana | $74.86 | -0.97% |

**🔭 NASA:** [Six Moons of Saturn](https://apod.nasa.gov/apod/image/2608/2026-08-05-0609_7-SaturnSystem_c.jpg)

**🚗 Car news:** [Dodge's CEO Says The Best Is Yet To Come: 'We're Going To Go Faster'](https://www.motor1.com/news/804511/dodge-ceo-charger-super-bee-interview/)

**📜 On this day, -3114:** The Mesoamerican Long Count calendar, used by several pre-Columbian Mesoamerican civilizations, notably the Maya, begins. — [32nd century BC](https://en.wikipedia.org/wiki/32nd_century_BC)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 9 repos · 4 followers

<!-- LATEST:END -->
