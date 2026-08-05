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
### 📅 Latest snapshot — 2026-08-05

> *"It is the nature of the wise to resist pleasures, but the foolish to be a slave to them."* — **Epictetus**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $64,523 | +0.81% |
| Ethereum | $1,890.66 | +1.08% |
| Solana | $74.14 | +0.29% |

**🔭 NASA:** [Spokes on Saturn's B Ring](https://apod.nasa.gov/apod/image/2608/saturn_spokes.gif)

**🚗 Car news:** [Car Buyers Don’t Want More Tech. They Just Want Heated Seats](https://www.motor1.com/news/803908/most-wanted-new-car-features/)

**📜 On this day, 25:** Guangwu claims the throne as Emperor of China, restoring the Han dynasty after the collapse of the short-lived Xin dynasty. — [20s](https://en.wikipedia.org/wiki/20s)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 7 repos · 0 followers

<!-- LATEST:END -->
