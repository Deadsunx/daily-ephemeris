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
### 📅 Latest snapshot — 2026-11-16

> *"I dream my painting and I paint my dream."* — **Vincent van Gogh**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $63,938 | -2.15% |
| Ethereum | $1,791.73 | -2.0% |
| Solana | $70.67 | -2.55% |

**🚗 Car news:** [BMW Recalls 720,000 Vehicles For Water Pump Fire Risk. Owners Told To Park Outside](https://www.motor1.com/news/815578/bmw-recall-26v733000-warning/)

**📜 On this day, 534:** The second edition of the Code of Justinian is issued by the Byzantine jurist Tribonian and his assistants, consisting of twelve updated and revised books. — [Code of Justinian](https://en.wikipedia.org/wiki/Code_of_Justinian)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 8 followers

<!-- LATEST:END -->
