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
### 📅 Latest snapshot — 2026-08-07

> *"Ability is a poor man's wealth."* — **John Wooden**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $64,878 | +0.34% |
| Ethereum | $1,913.58 | +0.02% |
| Solana | $73.71 | +0.46% |

**🔭 NASA:** [Rubin's COSMOS field](https://apod.nasa.gov/apod/image/2608/noirlab2618b_1024.jpg)

**🚗 Car news:** [Dodge Gives The 16-Year-Old Durango Special Colors And A  Two-Tone Concept](https://www.motor1.com/news/804124/dodge-durango-smokescreen-concept/)

**📜 On this day, 461:** Roman Emperor Majorian is beheaded near the river Iria in north-west Italy following his arrest and deposition by the magister militum Ricimer. — [Majorian](https://en.wikipedia.org/wiki/Majorian)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 7 repos · 2 followers

<!-- LATEST:END -->
