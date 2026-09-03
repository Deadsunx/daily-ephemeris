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
### 📅 Latest snapshot — 2026-09-03

> *"If you don't find the time, if you don't do the work, you don't get the results."* — **Arnold Schwarzenegger**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $77,834 | +0.73% |
| Ethereum | $2,401.18 | -0.53% |
| Solana | $100.62 | +0.9% |

**🔭 NASA:** [The Eclipse and the Stork](https://apod.nasa.gov/apod/image/2609/eclipse_stork_1080.jpg)

**🚗 Car news:** [Audi Boss: The More Expensive The Car, The More Buyers Want A Gas Engine](https://www.motor1.com/news/806982/audi-ceo-wealthy-buyers-want-engines/)

**📜 On this day, -36:** In the Battle of Naulochus, Marcus Vipsanius Agrippa, admiral of Octavian, defeats Sextus Pompey, son of Pompey, thus ending Pompeian resistance to the Second Triumvirate. — [Battle of Naulochus](https://en.wikipedia.org/wiki/Battle_of_Naulochus)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
