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
### 📅 Latest snapshot — 2026-09-08

> *"High thoughts must have high language."* — **Aristophanes**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $78,461 | -0.88% |
| Ethereum | $2,486.83 | -0.13% |
| Solana | $103.39 | -0.52% |

**🔭 NASA:** [Hubble: Decagon Around Saturn's South Pole](https://apod.nasa.gov/apod/image/2609/SaturnDecagon_Hubble_960.jpg)

**🚗 Car news:** [GM Prepping Big Powertrain Shakeup For Its HD Trucks: Report](https://www.motor1.com/news/807536/general-motors-heavy-duty-trucks-updated-powertrains/)

**📜 On this day, 14:** The funeral of Augustus takes place. His body is cremated and placed in his mausoleum. — [10s](https://en.wikipedia.org/wiki/10s)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
