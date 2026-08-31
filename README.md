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
### 📅 Latest snapshot — 2026-08-31

> *"To a mind that is still, the entire universe surrenders."* — **Zhuangzi**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $78,835 | +0.4% |
| Ethereum | $2,472.54 | -0.11% |
| Solana | $103.41 | -0.63% |

**🔭 NASA:** [Launch of the Roman Space Telescope](https://apod.nasa.gov/apod/image/2608/RomanLaunch_NASA.mp4)

**🚗 Car news:** [Ford Bronco Sport And Maverick Get Price Cuts For 2027, But Lose Some Features](https://www.motor1.com/news/806649/2027-ford-bronco-sport-maverick-pricing/)

**📜 On this day, 1056:** After a sudden gastric illness, Byzantine Empress Theodora dies childless, thus ending the Macedonian dynasty. — [List of Roman and Byzantine empresses](https://en.wikipedia.org/wiki/List_of_Roman_and_Byzantine_empresses)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 10 repos · 9 followers

<!-- LATEST:END -->
