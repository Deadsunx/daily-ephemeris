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
### 📅 Latest snapshot — 2026-11-15

> *"The weak can never forgive. Forgiveness is the attribute of the strong."* — **Mahatma Gandhi**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $65,481 | -2.51% |
| Ethereum | $1,835.04 | -3.74% |
| Solana | $72.59 | -4.34% |

**🚗 Car news:** [This Corvette Owner Bought A Brand-New C8. Then He Lost $37,000 After Just 570 Miles](https://www.motor1.com/news/815462/corvette-eray-massive-depreciation-auction/)

**📜 On this day, 655:** Battle of the Winwaed: Penda of Mercia is defeated by Oswiu of Northumbria. — [Battle of the Winwaed](https://en.wikipedia.org/wiki/Battle_of_the_Winwaed)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
