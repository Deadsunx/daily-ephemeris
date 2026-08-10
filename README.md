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
### 📅 Latest snapshot — 2026-08-10

> *"Correct what you can. Learn from what you can't."* — **Toni Morrison**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $64,973 | +0.35% |
| Ethereum | $1,915.67 | +0.14% |
| Solana | $76.57 | +0.84% |

**🔭 NASA:** [Three Galaxy Pairs](https://apod.nasa.gov/apod/image/2608/Three3GalaxyPairs_Sampaio_960.jpg)

**🚗 Car news:** [Volkswagen Could Finally Build A Pickup Truck For America: Report](https://www.motor1.com/news/804220/volkswagen-considering-pickup-truck-us/)

**📜 On this day, 654:** Pope Eugene I elected to succeed Martinus I. — [Pope Eugene I](https://en.wikipedia.org/wiki/Pope_Eugene_I)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 9 repos · 2 followers

<!-- LATEST:END -->
