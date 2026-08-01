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
### 📅 Latest snapshot — 2026-08-01

> *"Expect the best of yourself, and then do what is necessary to make it a reality."* — **Ralph Marston**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $62,975 | -2.12% |
| Ethereum | $1,866.4 | -2.02% |
| Solana | $72.92 | -1.87% |

**🔭 NASA:** [Buck Moon and Belt of Venus](https://apod.nasa.gov/apod/image/2608/FullMoon28-7-2026BrankoNadj1024.jpg)

**🚗 Car news:** [JLR's New North American CEO Has A Lot Of Work To Do](https://www.motor1.com/news/803393/jlr-new-north-american-ceo-appointed/)

**📜 On this day, -30:** Octavian (later known as Augustus) enters Alexandria, Egypt, executes Marcus Antonius Antyllus, and brings the city under the control of the Roman Republic. (date is O.S.) — [Augustus](https://en.wikipedia.org/wiki/Augustus)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 7 repos · 0 followers

<!-- LATEST:END -->
