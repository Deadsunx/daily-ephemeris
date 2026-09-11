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
### 📅 Latest snapshot — 2026-09-11

> *"It is secondary whether we choose belief or defiance. What is precious is that we are always able to choose."* — **Ming-Dao Deng**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $77,345 | -0.98% |
| Ethereum | $2,472.64 | +0.01% |
| Solana | $99.84 | -1.38% |

**🚗 Car news:** [BMW Celebrates Nürburgring Centenary With Six Limited-Edition M Cars](https://www.motor1.com/news/807927/bmw-m-cars-celebrate-100-years-nurburgring/)

**📜 On this day, 9:** The Battle of the Teutoburg Forest ends: The Roman Empire suffers the greatest defeat of its history and the Rhine is established as the border between the Empire and the so-called barbarians for the next four hundred years. — [0s](https://en.wikipedia.org/wiki/0s)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
