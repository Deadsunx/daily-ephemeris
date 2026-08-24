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
### 📅 Latest snapshot — 2026-08-24

> *"The quicker you let go of old cheese, the sooner you find new cheese."* — **Spencer Johnson**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $79,687 | +2.99% |
| Ethereum | $2,497.98 | +1.98% |
| Solana | $97.15 | +1.66% |

**🔭 NASA:** [Comet 220P in Outburst](https://apod.nasa.gov/apod/image/2608/Comet220P_SA_960.jpg)

**🚗 Car news:** [Lamborghini Isn't Worried About China... Yet](https://www.motor1.com/news/805908/lamborghini-ceo-china-not-threat/)

**📜 On this day, 367:** Gratian, son of Roman Emperor Valentinian I, is named co-Augustus at the age of eight by his father. — [Gratian](https://en.wikipedia.org/wiki/Gratian)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 10 repos · 9 followers

<!-- LATEST:END -->
