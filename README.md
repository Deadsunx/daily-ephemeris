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
### 📅 Latest snapshot — 2026-09-24

> *"You are what you believe in. You become that which you believe you can become."* — **Bhagavad Gita**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $84,418 | -0.06% |
| Ethereum | $2,694.19 | +0.65% |
| Solana | $117.33 | +2.41% |

**🔭 NASA:** [The Ghosts of Five Supernovas](https://apod.nasa.gov/apod/image/2609/5SNR_Auriga_1000.jpg)

**🚗 Car news:** [GM’s New Mongoose 8.3-Liter Duramax Diesel Makes 555 HP, 1,230 LB-FT](https://www.motor1.com/news/809471/gms-new-mongoose-duramax-diesel/)

**📜 On this day, 787:** The Second Council of Nicaea begins at the Church of Holy Wisdom in the city of Nicaea in Bithynia. — [AD 787](https://en.wikipedia.org/wiki/AD_787)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
