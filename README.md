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
### 📅 Latest snapshot — 2026-08-15

> *"Man suffers only because he takes seriously what the gods made for fun."* — **Alan Watts**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $63,022 | +0.04% |
| Ethereum | $1,882.72 | +0.18% |
| Solana | $75.38 | -0.22% |

**🔭 NASA:** [Bright Perseids from Sweden](https://apod.nasa.gov/apod/image/2608/PerseidsAPOD_P-MHeden.jpg)

**🚗 Car news:** [Gordon Murray S1 Is The Modern McLaren F1 We've Been Waiting For](https://www.motor1.com/news/805053/gordon-murray-s1-v12-manual/)

**📜 On this day, 636:** Arab–Byzantine wars: The Battle of Yarmouk between the Byzantine Empire and the Rashidun Caliphate begins. — [Arab–Byzantine wars](https://en.wikipedia.org/wiki/Arab%E2%80%93Byzantine_wars)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 9 repos · 4 followers

<!-- LATEST:END -->
