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
### 📅 Latest snapshot — 2026-11-25

> *"We have to live life with a sense of urgency so not a minute is wasted."* — **Les Brown**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $59,417 | -2.94% |
| Ethereum | $1,668.48 | -2.31% |
| Solana | $69.51 | -3.38% |

**🚗 Car news:** [Ineos Will Build Its Rugged Off-Roader In America Starting In 2028](https://www.motor1.com/news/816667/ineos-moving-production-to-us/)

**📜 On this day, -571:** Servius Tullius, king of Rome, celebrates the first of his three triumphs for his victory over the Etruscans. — [Servius Tullius](https://en.wikipedia.org/wiki/Servius_Tullius)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 7 followers

<!-- LATEST:END -->
