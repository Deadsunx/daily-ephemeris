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
### 📅 Latest snapshot — 2026-10-26

> *"Loving thoughts and actions are clearly beneficial for our physical and mental health."* — **Dalai Lama**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $80,429 | +0.37% |
| Ethereum | $2,331.28 | +0.3% |
| Solana | $101.36 | +0.81% |

**🔭 NASA:** [NASA Science](https://science.nasa.gov/wp-content/themes/nasa-child/assets/images/nasa-logo@2x.png)

**🚗 Car news:** [Acura ADX Gets Wild Custom Makeover Inspired By Vans And BMX Culture](https://www.motor1.com/news/813208/acura-adx-cz-77-concept/)

**📜 On this day, 1185:** The Uprising of Asen and Peter begins on the feast day of St. Demetrius of Thessaloniki and ends with the creation of the Second Bulgarian Empire. — [Uprising of Asen and Peter](https://en.wikipedia.org/wiki/Uprising_of_Asen_and_Peter)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 10 followers

<!-- LATEST:END -->
