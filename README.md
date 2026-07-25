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
### 📅 Latest snapshot — 2026-07-25

> *"It is amazing what you can accomplish if you do not care who gets the credit."* — **Harry S. Truman**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $63,916 | -2.26% |
| Ethereum | $1,853.5 | -2.04% |
| Solana | $73.6 | -3.09% |

**🔭 NASA:** [Tranquility and Serenity](https://apod.nasa.gov/apod/image/2607/TranquilitySerenity1024c.jpg)

**🚗 Car news:** [A Genesis Pickup Truck Could Be Back On The Table Thanks To Hyundai](https://www.motor1.com/news/802709/genesis-considering-pickup-truck/)

**📜 On this day, 306:** Constantine I is proclaimed Roman emperor by his troops. — [Constantine the Great](https://en.wikipedia.org/wiki/Constantine_the_Great)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 8 repos · 0 followers

<!-- LATEST:END -->
