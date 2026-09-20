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
### 📅 Latest snapshot — 2026-09-20

> *"A person without a sense of humor is like a wagon without springs, jolted by every pebble in the road."* — **Henry Ward Beecher**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $80,214 | -1.32% |
| Ethereum | $2,572.43 | -2.79% |
| Solana | $107.92 | -3.88% |

**🔭 NASA:** [Analemma over the Callanish Stones](https://apod.nasa.gov/apod/image/2609/CallanishAnalemma_Petricca_960.jpg)

**🚗 Car news:** [Jeremy Clarkson Is Selling Three Of His Most Famous Grand Tour Cars](https://www.motor1.com/news/808816/jeremy-clarkson-selling-grand-tour-cars/)

**📜 On this day, 1058:** Agnes of Poitou and Andrew I of Hungary meet to negotiate about the border territory of Burgenland. — [Agnes of Poitou](https://en.wikipedia.org/wiki/Agnes_of_Poitou)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
