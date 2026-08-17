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
### 📅 Latest snapshot — 2026-08-17

> *"Your happiness is what truly matters most. Do what you have to do in order to be happy."* — **Brian Tracy**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $63,428 | +0.56% |
| Ethereum | $1,900.29 | +1.0% |
| Solana | $75.48 | -0.01% |

**🔭 NASA:** [A Golden Corona Eclipse](https://apod.nasa.gov/apod/image/2608/GoldCorona_Santos_960.jpg)

**🚗 Car news:** [Gordon Murray S1 Is The Modern McLaren F1 We've Been Waiting For](https://www.motor1.com/news/805053/gordon-murray-s1-v12-manual/)

**📜 On this day, 986:** Byzantine–Bulgarian wars: Battle of the Gates of Trajan: The Bulgarians under the Comitopuli Samuel and Aron defeat the Byzantine forces at the Gate of Trajan, with Byzantine Emperor Basil II barely escaping. — [Byzantine–Bulgarian wars](https://en.wikipedia.org/wiki/Byzantine%E2%80%93Bulgarian_wars)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 9 repos · 6 followers

<!-- LATEST:END -->
