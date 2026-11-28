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
### 📅 Latest snapshot — 2026-11-28

> *"High thoughts must have high language."* — **Aristophanes**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $59,238 | -3.71% |
| Ethereum | $1,648.72 | -4.17% |
| Solana | $70.86 | -3.02% |

**🔭 NASA:** [NASA Science](https://science.nasa.gov/wp-content/themes/nasa-child/assets/images/nasa-logo@2x.png)

**🚗 Car news:** [Michael Schumacher’s Porsche Carrera GT Is Going to Auction With A Remarkable Paper Trail](https://www.motor1.com/news/817030/michael-schumacher-porsche-carrera-gt/)

**📜 On this day, 587:** Treaty of Andelot: King Guntram of Burgundy recognizes Childebert II as his heir. — [Treaty of Andelot](https://en.wikipedia.org/wiki/Treaty_of_Andelot)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 7 followers

<!-- LATEST:END -->
