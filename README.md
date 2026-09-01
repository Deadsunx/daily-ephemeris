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
### 📅 Latest snapshot — 2026-09-01

> *"Stop wasting time defending your problems and work on addressing them instead."* — **Celestine Chua**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $77,159 | -2.56% |
| Ethereum | $2,414.05 | -2.93% |
| Solana | $99.64 | -4.69% |

**🔭 NASA:** [A Plane Lunar Eclipse](https://apod.nasa.gov/apod/image/2608/PlaneEclipse_Ferreira_1059.jpg)

**🚗 Car news:** [Ford Recalls Nearly 150,000 Mustangs For Wiring Issue](https://www.motor1.com/news/806784/ford-mustang-engine-wiring-harness-recall/)

**📜 On this day, -396:** The Temple of Juno Regina (Aventine) is dedicated in Rome by Marcus Furius Camillus. — [Temple of Juno Regina (Aventine)](https://en.wikipedia.org/wiki/Temple_of_Juno_Regina_(Aventine))

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 10 repos · 9 followers

<!-- LATEST:END -->
