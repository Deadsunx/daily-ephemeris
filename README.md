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
### 📅 Latest snapshot — 2026-10-19

> *"The secret of change is to focus all your energy not on fighting the old, but on building the new."* — **Colin R. Davis**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $82,882 | +1.23% |
| Ethereum | $2,438.92 | +0.97% |
| Solana | $105.79 | +2.05% |

**🚗 Car news:** [Fiat's Tiny Topolino EV Is Already Earning Accolades](https://www.motor1.com/news/812394/time-chose-fiat-topolino/)

**📜 On this day, -202:** Second Punic War: At the Battle of Zama, Roman legions under Scipio Africanus defeat Hannibal Barca, leader of the army defending Carthage.[citation needed] — [Second Punic War](https://en.wikipedia.org/wiki/Second_Punic_War)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 11 followers

<!-- LATEST:END -->
