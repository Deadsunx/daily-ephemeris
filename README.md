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
### 📅 Latest snapshot — 2026-11-22

> *"Peace is not the absence of conflict, but the ability to cope with it."* — **Unknown**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $61,087 | +5.15% |
| Ethereum | $1,709.21 | +3.67% |
| Solana | $70.53 | +2.64% |

**🚗 Car news:** [Ferrari's New 296 Challenge Stradale Is A 670-HP Race Car You Can Drive Home](https://www.motor1.com/news/816314/ferrari-296-challenge-stradale-first-look-debut/)

**📜 On this day, 498:** After the death of Anastasius II, Symmachus is elected Pope in the Lateran Palace, while Laurentius is elected Pope in Santa Maria Maggiore. — [Pope Anastasius II](https://en.wikipedia.org/wiki/Pope_Anastasius_II)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 8 followers

<!-- LATEST:END -->
