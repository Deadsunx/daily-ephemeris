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
### 📅 Latest snapshot — 2026-10-14

> *"Genius is one percent inspiration and ninety-nine percent perspiration."* — **Thomas Edison**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $83,378 | -0.1% |
| Ethereum | $2,504.24 | -0.35% |
| Solana | $106.96 | -0.52% |

**🚗 Car news:** [F1 Is Returning To Africa With A New Track](https://www.motor1.com/news/811886/formula-1-rwanda-grand-prix/)

**📜 On this day, 996:** Al-Hakim bi-Amr Allah becomes caliph. He is the first Fatimid ruler to have been born in Egypt and arguably the most controversial member of the dynasty. — [Al-Hakim bi-Amr Allah](https://en.wikipedia.org/wiki/Al-Hakim_bi-Amr_Allah)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 12 followers

<!-- LATEST:END -->
