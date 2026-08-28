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
### 📅 Latest snapshot — 2026-08-28

> *"Whatever you decide to do, make sure it makes you happy."* — **Paulo Coelho**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $78,874 | -1.84% |
| Ethereum | $2,493.61 | -1.13% |
| Solana | $106.09 | -0.83% |

**🔭 NASA:** [The Sky Turns Above Paranal](https://apod.nasa.gov/apod/image/2608/TheSkyTurnsAboveParanal_1024.jpg)

**🚗 Car news:** [This Is The Mustang We Wish Ford Would Build](https://www.motor1.com/news/806411/ford-mustang-future-rendering-by-luca-serafini/)

**📜 On this day, 475:** The Roman general Orestes forces western Roman Emperor Julius Nepos to flee his capital city, Ravenna. — [Roman Empire](https://en.wikipedia.org/wiki/Roman_Empire)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 10 repos · 9 followers

<!-- LATEST:END -->
