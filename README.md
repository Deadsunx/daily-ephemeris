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
### 📅 Latest snapshot — 2026-08-28

> *"Whatever you decide to do, make sure it makes you happy."* — **Paulo Coelho**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $80,429 | +1.97% |
| Ethereum | $2,516.69 | +0.8% |
| Solana | $109.58 | +8.42% |

**🚗 Car news:** [GTA 6 Is Finally Getting Real Racing (Update)](https://www.motor1.com/news/806207/grand-theft-auto-6-race-track-leaked/)

**📜 On this day, 475:** The Roman general Orestes forces western Roman Emperor Julius Nepos to flee his capital city, Ravenna. — [Roman Empire](https://en.wikipedia.org/wiki/Roman_Empire)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 10 repos · 9 followers

<!-- LATEST:END -->
