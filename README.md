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
### 📅 Latest snapshot — 2026-09-16

> *"Move out of your comfort zone. You can only grow if you are willing to feel awkward and uncomfortable when you try something new."* — **Brian Tracy**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $75,615 | -1.72% |
| Ethereum | $2,399.17 | -3.11% |
| Solana | $96.83 | -3.75% |

**🔭 NASA:** [Webb's View of M64](https://apod.nasa.gov/apod/image/2609/M64_Webb_1024.jpg)

**🚗 Car news:** [Ford Mustang GTD Gives Europe A Second Chance At The Wildest Pony](https://www.motor1.com/news/808460/ford-mustang-gtd-europe-application/)

**📜 On this day, 681:** Pope Honorius I is posthumously excommunicated by the Sixth Ecumenical Council. — [Pope Honorius I](https://en.wikipedia.org/wiki/Pope_Honorius_I)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 8 followers

<!-- LATEST:END -->
