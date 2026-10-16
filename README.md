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
### 📅 Latest snapshot — 2026-10-16

> *"As we first succeed, we will find ourselves in new situations, facing new problems."* — **Ryan Holiday**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $82,233 | +1.24% |
| Ethereum | $2,457.76 | +3.55% |
| Solana | $106.63 | +3.47% |

**🚗 Car news:** [The New Tesla Roadster Looks Nothing Like The Concept](https://www.motor1.com/news/812197/new-tesla-roadster-design/)

**📜 On this day, 456:** Ricimer defeats Avitus at Piacenza and becomes master of the Western Roman Empire. — [Ricimer](https://en.wikipedia.org/wiki/Ricimer)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 12 followers

<!-- LATEST:END -->
