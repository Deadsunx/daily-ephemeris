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
### 📅 Latest snapshot — 2026-09-21

> *"The smallest act of kindness is worth more than the greatest intention."* — **Kahlil Gibran**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $86,772 | +6.95% |
| Ethereum | $2,772.29 | +5.37% |
| Solana | $118.52 | +7.47% |

**🔭 NASA:** [Cocoon Nebula Wide Field](https://apod.nasa.gov/apod/image/2609/Cocoon_Czerski_1080.jpg)

**🚗 Car news:** [Porsche Is Working On An Automatic That Pretends To Be A Manual](https://www.motor1.com/news/808978/porsche-simulated-manual-transmission-patent/)

**📜 On this day, 454:** Western Roman Emperor Valentinian III murders his general Flavius Aetius on instigation of eunuch Heraclius and senator Petronius Maximus. — [Roman emperor](https://en.wikipedia.org/wiki/Roman_emperor)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
