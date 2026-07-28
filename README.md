# Daily Data Archive 🌍

A small project that builds a **growing dataset** by fetching four free sources
every single day and archiving them — all automatically via a scheduled
[GitHub Actions](https://docs.github.com/actions) workflow.

Because the automation runs on **GitHub's servers**, the daily commit happens
whether my laptop is on or off.

**🌐 Live page → https://deadsunx.github.io/un-peu-trop-secret/**
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
### 📅 Latest snapshot — 2026-07-28

> *"Be kind, for everyone you meet is fighting a harder battle."* — **Plato**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $63,736 | -1.92% |
| Ethereum | $1,910.0 | -1.7% |
| Solana | $73.91 | -2.84% |

**🔭 NASA:** [Barnards Loop over Twin Volcanoes](https://apod.nasa.gov/apod/image/2607/LoopVolcanos_Laserna_960.jpg)

**🚗 Car news:** [Spied: Mercedes-AMG GT Black Series Shows Off Its Big Wing And V8 Sound](https://www.motor1.com/news/802997/mercedes-amg-gt-black-series-spied-v8-engine/)

**📜 On this day, 484:** Pope Felix III excommunicated patriarch Acacius of Constantinople for his support of the Henoticon and his support of the removal of patriarch John Talaia, leading to the Acacian schism. — [Pope Felix III](https://en.wikipedia.org/wiki/Pope_Felix_III)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 9 repos · 0 followers

<!-- LATEST:END -->
