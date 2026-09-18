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
### 📅 Latest snapshot — 2026-09-18

> *"Till it has loved, no man or woman can become itself."* — **Emily Dickinson**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $77,911 | +1.98% |
| Ethereum | $2,495.27 | +2.32% |
| Solana | $105.75 | +5.59% |

**🔭 NASA:** [Messier 33: The Triangulum Galaxy](https://apod.nasa.gov/apod/image/2609/m33m14_rasa3NM1024.jpg)

**🚗 Car news:** [Max Verstappen Cruises Monaco Streets In Tuned ABT Audi RS6 Avant](https://www.motor1.com/news/808726/max-verstappen-abt-audi-rs6/)

**📜 On this day, 96:** Emperor Domitian is assassinated as a result of a plot by his wife Domitia and two Praetorian prefects. Nerva is then proclaimed as his successor. — [AD 96](https://en.wikipedia.org/wiki/AD_96)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
