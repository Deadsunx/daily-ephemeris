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
### 📅 Latest snapshot — 2026-08-16

> *"Motivation is what gets you started. Habit is what keeps you going."* — **Jim Rohn**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $63,100 | +0.05% |
| Ethereum | $1,882.22 | -0.01% |
| Solana | $75.52 | +0.02% |

**🔭 NASA:** [Milky Way over Yellowstone](https://apod.nasa.gov/apod/image/2608/mwyellowstone_lane_960.jpg)

**🚗 Car news:** [Gordon Murray S1 Is The Modern McLaren F1 We've Been Waiting For](https://www.motor1.com/news/805053/gordon-murray-s1-v12-manual/)

**📜 On this day, -1:** Wang Mang consolidates his power in China and is declared marshal of state. Emperor Ai of Han, who died the previous day, had no heirs. — [Wang Mang](https://en.wikipedia.org/wiki/Wang_Mang)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 9 repos · 4 followers

<!-- LATEST:END -->
