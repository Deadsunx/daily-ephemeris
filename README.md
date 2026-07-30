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
### 📅 Latest snapshot — 2026-07-30

> *"It isn't that they can't see the solution. It is that they can't see the problem."* — **Gilbert Chesterton**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $63,923 | -0.23% |
| Ethereum | $1,900.93 | -0.54% |
| Solana | $73.52 | -0.18% |

**🔭 NASA:** [Red Sun through Wildfire Smoke](https://apod.nasa.gov/apod/image/2607/red_sun_1024.jpg)

**🚗 Car news:** [Mini Is Testing Its Most Off-Road-Capable SUV Yet](https://www.motor1.com/news/803145/mini-countryman-edition-brand-toughest/)

**📜 On this day, -30:** Mark Antony wins a final cavalry battle against Octavian in the battle of Alexandria, but his infantry is defeated and the next day his fleet and troops start to desert to Octavian. — [Mark Antony](https://en.wikipedia.org/wiki/Mark_Antony)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 6 repos · 0 followers

<!-- LATEST:END -->
