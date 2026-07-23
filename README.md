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
### 📅 Latest snapshot — 2026-07-23

> *"You have the potential for greatness."* — **Steve Harvey**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $65,616 | -0.46% |
| Ethereum | $1,920.91 | +0.14% |
| Solana | $77.4 | +0.26% |

**🔭 NASA:** [The Large Magellanic Cloud](https://apod.nasa.gov/apod/image/2607/LMC_1024.jpg)

**🚗 Car news:** [Gotcha: Toyota's New Mid-Engine Sports Car Possibly Caught Testing On Video](https://www.motor1.com/news/802471/toyota-celica-sports-car-caught-testing-fuji/)

<!-- LATEST:END -->
