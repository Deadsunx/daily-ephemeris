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
### 📅 Latest snapshot — 2026-08-06

> *"Talk sense to a fool and he calls you foolish."* — **Euripides**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $64,698 | +0.7% |
| Ethereum | $1,908.71 | +2.15% |
| Solana | $73.94 | -0.11% |

**🔭 NASA:** [New Sharpest Image of the Sun Uncovers Instability](https://apod.nasa.gov/apod/image/2608/SunFlowers_NSO_960.jpg)

**🚗 Car news:** [Seven Dream Ferraris Are Headed To Auction, From the 288 GTO To The Luce](https://www.motor1.com/news/803757/rare-ferrari-auction-monterey-288-gto-luce/)

**📜 On this day, 258:** Pope Sixtus II is arrested while celebrating mass and then beheaded with several of his deacons. — [Pope Sixtus II](https://en.wikipedia.org/wiki/Pope_Sixtus_II)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 7 repos · 1 followers

<!-- LATEST:END -->
