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
### 📅 Latest snapshot — 2026-09-28

> *"One mistake does not have to rule a person's entire life."* — **Joyce Meyer**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $83,412 | -1.39% |
| Ethereum | $2,678.21 | -0.31% |
| Solana | $118.24 | -3.74% |

**🔭 NASA:** [Cosmic Latte: The Average Color of the Universe](https://apod.nasa.gov/apod/image/2609/CosmicLatte_jhu_960_annotated.jpg)

**🚗 Car news:** [Rezvani Made A Ferrari 'Manual' Kit For $25,000. There's No Clutch](https://www.motor1.com/news/801058/ferrari-manual-quick-shift-rezvani/)

**📜 On this day, -48:** Pompey disembarks at Pelusium upon arriving in Egypt, whereupon he is assassinated by order of King Ptolemy XIII. — [Pompey](https://en.wikipedia.org/wiki/Pompey)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
