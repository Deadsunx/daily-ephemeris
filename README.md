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
### 📅 Latest snapshot — 2026-09-07

> *"The greatest treasures are those invisible to the eye but found by the heart."* — **Judy Garland**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $79,468 | -0.38% |
| Ethereum | $2,492.25 | -0.03% |
| Solana | $104.76 | -0.41% |

**🔭 NASA:** [The Pelican Nebula in Gas, Dust, and Stars](https://apod.nasa.gov/apod/image/2609/Pelican_Killion_960.jpg)

**🚗 Car news:** [Mercedes-AMG CLE Mythos: The 641-HP V8 Super Coupe Is Coming](https://www.motor1.com/news/807319/mercedes-cle-v8-news/)

**📜 On this day, 878:** Louis the Stammerer is crowned as king of West Francia by Pope John VIII. — [Louis the Stammerer](https://en.wikipedia.org/wiki/Louis_the_Stammerer)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
