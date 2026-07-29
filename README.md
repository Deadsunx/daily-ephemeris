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
### 📅 Latest snapshot — 2026-07-29

> *"If you let your head get too big, it'll break your neck."* — **Elvis Presley**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $63,762 | -0.02% |
| Ethereum | $1,896.3 | -0.9% |
| Solana | $73.31 | -1.02% |

**🔭 NASA:** [Psyche Receives Gravity Assist from Mars](https://www.youtube.com/embed/6_cH5-daLjg?si=i9geSInQj3VMZwx3)

**🚗 Car news:** [This Lovely Mercedes 190 Evo II Restomod Packs 765 Horsepower](https://www.motor1.com/news/803134/mercedes-benz-evo-ii-restomod/)

**📜 On this day, -587:** The Neo-Babylonian Empire sacks Jerusalem and destroys the First Temple. — [Neo-Babylonian Empire](https://en.wikipedia.org/wiki/Neo-Babylonian_Empire)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 6 repos · 0 followers

<!-- LATEST:END -->
