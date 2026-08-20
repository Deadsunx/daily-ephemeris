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
### 📅 Latest snapshot — 2026-08-20

> *"No matter how tall the mountain is, it cannot block the sun."* — **Chinese Proverb**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $69,315 | +7.77% |
| Ethereum | $2,253.69 | +17.93% |
| Solana | $84.56 | +9.77% |

**🔭 NASA:** [The Elephant's Trunk in Cepheus](https://apod.nasa.gov/apod/image/2608/IMG_5201_sgarbossa1024.jpeg)

**🚗 Car news:** [2027 Genesis GV90 Debuts As A Flagship SUV With Coach Doors](https://www.motor1.com/news/805518/2027-genesis-gv90-horsepower-price-details/)

**📜 On this day, 14:** Agrippa Postumus, maternal grandson of the late Roman emperor Augustus, is executed by his guards while in exile. — [10s](https://en.wikipedia.org/wiki/10s)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 10 repos · 6 followers

<!-- LATEST:END -->
