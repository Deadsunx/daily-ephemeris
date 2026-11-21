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
### 📅 Latest snapshot — 2026-11-21

> *"To avoid criticism, do nothing, say nothing, and be nothing."* — **Elbert Hubbard**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $58,077 | -5.97% |
| Ethereum | $1,650.11 | -5.57% |
| Solana | $68.67 | -4.21% |

**🚗 Car news:** [BYD's Boxy SUV Banned In The EU After Land Rover Defender Copycat Ruling](https://www.motor1.com/news/816327/byd-ti7-banned-eu-defender-design-copy/)

**📜 On this day, -164:** Judas Maccabeus, son of Mattathias of the Hasmonean family, rededicates the Temple in Jerusalem, an event that is commemorated each year by the festival of Hanukkah. (25 Kislev 3597 in the Hebrew calendar.) — [Judas Maccabeus](https://en.wikipedia.org/wiki/Judas_Maccabeus)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 8 followers

<!-- LATEST:END -->
