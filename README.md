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
### 📅 Latest snapshot — 2026-08-27

> *"Bad things are not the worst things that an happen to us. NOTHING is the worst thing that can happen to us."* — **Richard Bach**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $80,136 | +2.81% |
| Ethereum | $2,514.26 | +2.81% |
| Solana | $106.95 | +11.77% |

**🔭 NASA:** [Colorful Aurora over Icelandic Waterfall](https://apod.nasa.gov/apod/image/2608/Aurora_over_Fall_800.jpg)

**🚗 Car news:** [Meet the Indecent 009: An Extreme Italian Take On The Porsche 911](https://www.motor1.com/news/806274/porsche-911-air-suspension-italy/)

**📜 On this day, 410:** The sacking of Rome by the Visigoths ends after three days. — [Sack of Rome (410)](https://en.wikipedia.org/wiki/Sack_of_Rome_(410))

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 10 repos · 9 followers

<!-- LATEST:END -->
