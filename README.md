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
### 📅 Latest snapshot — 2026-07-27

> *"But better die than live mechanically a life that is a repetition of repetitions."* — **D. H. Lawrence**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $65,376 | +1.55% |
| Ethereum | $1,967.9 | +4.47% |
| Solana | $76.64 | +2.19% |

**🔭 NASA:** [NGC 7635: The Bubble Nebula](https://apod.nasa.gov/apod/image/2607/Bubble_Piechnik_960.jpg)

**🚗 Car news:** [Lexus Has The Happiest Dealers In America. Infiniti Doesn't](https://www.motor1.com/news/802716/lexus-happiest-dealerships-amerca/)

**📜 On this day, 1054:** Siward, Earl of Northumbria, invades Scotland and defeats Macbeth, King of Scotland, somewhere north of the Firth of Forth. This is known as the Battle of Dunsinane. — [Siward, Earl of Northumbria](https://en.wikipedia.org/wiki/Siward%2C_Earl_of_Northumbria)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 9 repos · 0 followers

<!-- LATEST:END -->
