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
### 📅 Latest snapshot — 2026-10-01

> *"When you stop questioning, you stop learning."* — **Lolly Daskal**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $83,726 | -0.13% |
| Ethereum | $2,690.83 | -0.17% |
| Solana | $117.61 | -1.82% |

**🔭 NASA:** [NASA Science](https://science.nasa.gov/wp-content/themes/nasa-child/assets/images/nasa-logo@2x.png)

**🚗 Car news:** [Want A Tesla Model Y? You'll Have To Wait](https://www.motor1.com/news/810433/tesla-model-y-wait-times/)

**📜 On this day, -331:** Alexander the Great defeats Darius III of Persia in the Battle of Gaugamela. — [Alexander the Great](https://en.wikipedia.org/wiki/Alexander_the_Great)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 10 followers

<!-- LATEST:END -->
