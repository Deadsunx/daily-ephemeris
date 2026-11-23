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
### 📅 Latest snapshot — 2026-11-23

> *"Have a vision. Be demanding."* — **Colin Powell**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $61,080 | +0.7% |
| Ethereum | $1,718.47 | +1.02% |
| Solana | $72.36 | +3.35% |

**🚗 Car news:** [Subaru's American-Built Ascent Is Heading To Japan](https://www.motor1.com/news/816461/subaru-ascent-japan-launch/)

**📜 On this day, -534:** Thespis of Icaria becomes the first recorded actor to portray a character on stage. — [Thespis](https://en.wikipedia.org/wiki/Thespis)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 8 followers

<!-- LATEST:END -->
