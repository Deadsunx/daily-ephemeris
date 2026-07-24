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
### 📅 Latest snapshot — 2026-07-24

> *"Change is hard at first, messy in the middle and gorgeous at the end."* — **Robin Sharma**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $64,155 | -1.1% |
| Ethereum | $1,860.39 | -1.07% |
| Solana | $73.9 | -2.41% |

**🔭 NASA:** [RCW 86: Historical Supernova Remnant](https://apod.nasa.gov/apod/image/2607/RCW86Final1024.jpg)

**🚗 Car news:** [The New BMW X5 Costs Over $95,000 With Every Option](https://www.motor1.com/news/802685/2027-bmw-x5-configurator-mot-expensive/)

**📜 On this day, 1132:** Battle of Nocera between Ranulf II of Alife and Roger II of Sicily. — [Battle of Nocera](https://en.wikipedia.org/wiki/Battle_of_Nocera)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 8 repos · 0 followers

<!-- LATEST:END -->
