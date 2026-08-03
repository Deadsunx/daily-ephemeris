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
### 📅 Latest snapshot — 2026-08-03

> *"It all depends on what you choose to believe."* — **Spencer Johnson**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $63,855 | +0.92% |
| Ethereum | $1,868.11 | +0.03% |
| Solana | $73.67 | +0.48% |

**🔭 NASA:** [Vaporizing Meteor Photobombs the Lacerta Nebula](https://apod.nasa.gov/apod/image/2608/MeteorGecko_Burnett_1080.jpg)

**🚗 Car news:** [Lamborghini Honors A Legendary Supercar With Some Fancy Paint](https://www.motor1.com/news/803585/lamborghini-revuelto-miura-homage-package/)

**📜 On this day, 8:** Roman Empire general Tiberius defeats the Dalmatae on the river Bosna. — [0s](https://en.wikipedia.org/wiki/0s)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 7 repos · 0 followers

<!-- LATEST:END -->
