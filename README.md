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
### 📅 Latest snapshot — 2026-08-09

> *"Magic is believing in yourself, if you can do that, you can make anything happen."* — **Johann Wolfgang von Goethe**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $64,741 | -0.36% |
| Ethereum | $1,911.55 | -0.22% |
| Solana | $75.91 | +1.76% |

**🔭 NASA:** [Contemplating the Sun](https://apod.nasa.gov/apod/image/2608/sunsilhouettes_gilbert_960.jpg)

**🚗 Car news:** [Volkswagen Could Finally Build A Pickup Truck For America: Report](https://www.motor1.com/news/804220/volkswagen-considering-pickup-truck-us/)

**📜 On this day, -48:** Caesar's Civil War: Battle of Pharsalus: Julius Caesar decisively defeats Pompey at Pharsalus and Pompey flees to Egypt. — [Caesar's civil war](https://en.wikipedia.org/wiki/Caesar's_civil_war)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 8 repos · 2 followers

<!-- LATEST:END -->
