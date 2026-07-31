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
### 📅 Latest snapshot — 2026-07-31

> *"New beginnings are disguised as painful endings."* — **Lao Tzu**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $62,896 | -3.04% |
| Ethereum | $1,868.35 | -2.68% |
| Solana | $73.26 | -1.68% |

**🔭 NASA:** [NGC 4372 and the Dark Doodad](https://apod.nasa.gov/apod/image/2607/DARK-DOODAD_1024.jpg)

**🚗 Car news:** [This Trailer Drives Itself Into The Campsite](https://www.motor1.com/news/803378/aboard-t4-caravan-debut/)

**📜 On this day, 398:** End of the Gildonic rebellion after Gildo's forces are defeated by forces loyal to Western Roman Emperor Honorius under Gildo's brother Mascezel and Gildo's subsequent death. — [Gildonic War](https://en.wikipedia.org/wiki/Gildonic_War)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 7 repos · 0 followers

<!-- LATEST:END -->
