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
### 📅 Latest snapshot — 2026-10-22

> *"The secret of getting started is breaking your complex, overwhelming tasks into small manageable tasks, and then starting on the first one."* — **Mark Twain**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $81,305 | -3.82% |
| Ethereum | $2,382.03 | -4.57% |
| Solana | $103.38 | -4.5% |

**🚗 Car news:** [Ford Explains Why Naming Cars Is So Hard: 'Everyone Has An Opinion'](https://www.motor1.com/news/812896/ford-puts-every-car-name/)

**📜 On this day, -2137:** A solar eclipse occurs over China, one of the earliest recorded in human history, reportedly resulting in the executions of two astronomers who failed to predict it. — [Solar eclipse of October 22, 2137 BC](https://en.wikipedia.org/wiki/Solar_eclipse_of_October_22%2C_2137_BC)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 10 followers

<!-- LATEST:END -->
