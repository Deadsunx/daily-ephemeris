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
### 📅 Latest snapshot — 2026-09-17

> *"When things go wrong, don't go with them."* — **Elvis Presley**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $76,523 | +1.37% |
| Ethereum | $2,451.39 | +2.69% |
| Solana | $100.92 | +3.7% |

**🔭 NASA:** [A Treasure Chest in the Carina Nebula](https://apod.nasa.gov/apod/image/2609/JWST_Treasure_Chest_800.jpg)

**🚗 Car news:** [California Finally Eases Smog Rules For Classic Cars Thanks To 'Leno's Law'](https://www.motor1.com/news/808673/california-signs-lenos-law/)

**📜 On this day, 14:** The Roman Senate decides to deify the late emperor Augustus. — [10s](https://en.wikipedia.org/wiki/10s)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
