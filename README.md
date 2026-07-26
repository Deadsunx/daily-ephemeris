# Daily Data Archive 🌍

A small project that builds a **growing dataset** by fetching four free sources
every single day and archiving them — all automatically via a scheduled
[GitHub Actions](https://docs.github.com/actions) workflow.

Because the automation runs on **GitHub's servers**, the daily commit happens
whether my laptop is on or off.

**🌐 Live page → https://deadsunx.github.io/un-peu-trop-secret/**
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
### 📅 Latest snapshot — 2026-07-26

> *"Let us rather run the risk of wearing out than rusting out."* — **Theodore Roosevelt**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $64,467 | +0.79% |
| Ethereum | $1,883.0 | +1.38% |
| Solana | $75.06 | +1.55% |

**🔭 NASA:** [Simulation TNG50: A Galaxy Cluster Forms](https://apod.nasa.gov/apod/image/2607/ClusterFormation_TNG50.mp4)

**🚗 Car news:** [This Is One Of The Rarest Mercedes G-Classes Ever Made, And It Just Sold For $143,000](https://www.motor1.com/news/802691/saudi-prince-mercedes-g-class-v8-amg/)

**📜 On this day, 657:** First Fitna: In the Battle of Siffin, troops led by Ali ibn Abu Talib clash with those led by Muawiyah I. — [First Fitna](https://en.wikipedia.org/wiki/First_Fitna)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 8 repos · 0 followers

<!-- LATEST:END -->
