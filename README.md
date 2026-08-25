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
### 📅 Latest snapshot — 2026-08-25

> *"Mistakes are painful when they happen, but years later a collection of mistakes is what is called experience."* — **Denis Waitley**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $80,255 | +3.94% |
| Ethereum | $2,494.64 | +2.02% |
| Solana | $101.49 | +7.64% |

**🔭 NASA:** [Earth's Shadow Visualized with Lunar Eclipses](https://apod.nasa.gov/apod/image/2608/EarthShadow_Martin_960.jpg)

**🚗 Car news:** [Another State Is Raising Speed Limits To 75 Miles Per Hour](https://www.motor1.com/news/805928/missouri-speed-limits-75-mph/)

**📜 On this day, 383:** Roman Emperor Gratian is murdered at a banquet after having surrendered to the forces of rival emperor Magnus Maximus. — [AD 383](https://en.wikipedia.org/wiki/AD_383)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 10 repos · 9 followers

<!-- LATEST:END -->
