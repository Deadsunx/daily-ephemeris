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
### 📅 Latest snapshot — 2026-09-23

> *"When we strive to become better than we are, everything around us becomes better, too."* — **Paulo Coelho**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $84,368 | -2.45% |
| Ethereum | $2,671.02 | -3.17% |
| Solana | $114.37 | -3.38% |

**🔭 NASA:** [A New Lunar Crater: McGetchin](https://apod.nasa.gov/apod/image/2609/mcgetchin_after.jpg)

**🚗 Car news:** [Bentley Says No To Front Passenger Screens: 'Technology Has To Add Value'](https://www.motor1.com/news/809010/bentley-passenger-screens-explained/)

**📜 On this day, 38:** Drusilla, Caligula's sister who died in June, with whom the emperor is said to have an incestuous relationship, is deified. — [30s](https://en.wikipedia.org/wiki/30s)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
