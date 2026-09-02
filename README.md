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
### 📅 Latest snapshot — 2026-09-02

> *"Force has no place where there is need of skill."* — **Herodotus**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $77,335 | +0.23% |
| Ethereum | $2,394.94 | -0.8% |
| Solana | $99.53 | -0.2% |

**🔭 NASA:** [Solar Eclipses and Culture](https://apod.nasa.gov/apod/image/2609/colors_of_eclipse_1024.jpg)

**🚗 Car news:** [The Subaru WRX Is Making A Huge Sales Comeback](https://www.motor1.com/news/806907/subaru-wrx-sales-august-2026/)

**📜 On this day, -44:** Pharaoh Cleopatra VII of Egypt declares her son co-ruler as Ptolemy XV Caesarion. — [Pharaoh](https://en.wikipedia.org/wiki/Pharaoh)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
