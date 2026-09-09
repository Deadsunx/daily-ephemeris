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
### 📅 Latest snapshot — 2026-09-09

> *"We are all like the bright moon, we still have our darker side."* — **Kahlil Gibran**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $78,447 | -0.05% |
| Ethereum | $2,481.5 | -0.34% |
| Solana | $103.32 | -0.21% |

**🔭 NASA:** [Witness XZ Andromedae Wink](https://apod.nasa.gov/apod/image/2609/xz_and.mp4)

**🚗 Car news:** [Ford Wants You To Sleep In Your Bronco](https://www.motor1.com/news/807713/ford-bronco-overland-camping-patents/)

**📜 On this day, 337:** Constantine II, Constantius II, and Constans succeed their father Constantine I as co-emperors. The Roman Empire is divided between the three Augusti. — [337](https://en.wikipedia.org/wiki/337)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
