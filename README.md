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
### 📅 Latest snapshot — 2026-08-12

> *"Sadness is but a wall between two gardens."* — **Kahlil Gibran**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $63,448 | -0.02% |
| Ethereum | $1,889.69 | +1.42% |
| Solana | $75.6 | +1.0% |

**🔭 NASA:** [Perseids Over a little Planet](https://apod.nasa.gov/apod/image/2608/A_Planet_of_Meteors_1024.jpg)

**🚗 Car news:** [McLaren Teases Its First Manual Supercar In Decades](https://www.motor1.com/news/804671/mclaren-teases-manual-supercar/)

**📜 On this day, 1099:** First Crusade: Battle of Ascalon: Crusaders under the command of Godfrey of Bouillon defeat Fatimid forces led by Al-Afdal Shahanshah. This is considered the last engagement of the First Crusade. — [First Crusade](https://en.wikipedia.org/wiki/First_Crusade)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 9 repos · 4 followers

<!-- LATEST:END -->
