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
### 📅 Latest snapshot — 2026-11-07

> *"The things I carry are my thoughts. That's it. They are the only weight. My thoughts determine whether I am free and light or burdened."* — **Kamal Ravikant**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $75,707 | -0.04% |
| Ethereum | $2,231.98 | +0.04% |
| Solana | $89.53 | -0.44% |

**🚗 Car news:** [Lego Has Competition. Hot Wheels Expands Its Brick Shop With New Buildable Sports Cars](https://www.motor1.com/news/814624/hot-wheels-buildable-brick-cars/)

**📜 On this day, 335:** Athanasius, 20th pope of Alexandria, is banished to Trier on the charge that he prevented a grain fleet from sailing to Constantinople. — [Athanasius of Alexandria](https://en.wikipedia.org/wiki/Athanasius_of_Alexandria)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
