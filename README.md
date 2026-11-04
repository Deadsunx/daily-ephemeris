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
### 📅 Latest snapshot — 2026-11-04

> *"What the eye doesn't see and the mind doesn't know, doesn't exist."* — **D. H. Lawrence**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $80,151 | +2.95% |
| Ethereum | $2,419.41 | +5.45% |
| Solana | $94.57 | +0.96% |

**🚗 Car news:** [Someone Stuffed A 13-Rotor Engine Into A Miata. And Yes, It Actually Runs](https://www.motor1.com/news/814432/13-rotor-miata-debuts-2026/)

**📜 On this day, 512:** Following Byzantine emperor Anastasius' deposition of Chalcedonian patriarchs and attempts to make Monophysite changes to liturgy, riots break out in Constantinople with a mob trying to proclaim Areobindus as emperor. — [List of Byzantine emperors](https://en.wikipedia.org/wiki/List_of_Byzantine_emperors)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 10 followers

<!-- LATEST:END -->
