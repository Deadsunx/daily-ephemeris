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
### 📅 Latest snapshot — 2026-09-12

> *"He who leaves the game wins it."* — **Nicolas Chamfort**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $77,313 | +0.21% |
| Ethereum | $2,526.38 | +2.51% |
| Solana | $101.7 | +2.2% |

**🔭 NASA:** [Apollo 11: Catching Some Sun](https://apod.nasa.gov/apod/image/2609/AS11-40-5872HR1024.jpg)

**🚗 Car news:** [Ram's Small Work Van Is Back For 2027 At Under $40,000](https://www.motor1.com/news/808014/2027-ram-promaster-city-price-trims-specs/)

**📜 On this day, -490:** Battle of Marathon: The conventionally accepted date for the Battle of Marathon. The Athenians and their Plataean allies defeat the first Persian invasion force of Greece. — [Battle of Marathon](https://en.wikipedia.org/wiki/Battle_of_Marathon)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
