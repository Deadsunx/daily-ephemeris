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
### 📅 Latest snapshot — 2026-09-19

> *"Make your mind your own business."* — **Jack Butcher**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $81,311 | +4.27% |
| Ethereum | $2,647.26 | +5.8% |
| Solana | $112.22 | +5.75% |

**🔭 NASA:** [A Zodiacal Night](https://apod.nasa.gov/apod/image/2609/2026-09-09ZodiacalLightHSP1024.jpg)

**🚗 Car news:** [Gas Prices Are Up, And So Are EV Sales](https://www.motor1.com/news/808800/new-used-ev-sales-rising/)

**📜 On this day, 96:** Nerva, suspected of complicity of the death of Domitian, is declared emperor by Senate. The Senate then annuls laws passed by Domitian and orders his statues to be destroyed. — [AD 96](https://en.wikipedia.org/wiki/AD_96)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
