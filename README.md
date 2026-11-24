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
### 📅 Latest snapshot — 2026-11-24

> *"The size of your success is measured by the strength of your desire; the size of your dream; and how you handle disappointment along the way."* — **Robert Kiyosaki**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $60,328 | -5.94% |
| Ethereum | $1,696.69 | -7.47% |
| Solana | $70.1 | -9.87% |

**🚗 Car news:** [Chrysler Recalls 82,843 Ram 1500 Trucks Over Brake Software Bug That Could Disable Safety Features](https://www.motor1.com/news/816607/ram-1500-classic-abs-recall/)

**📜 On this day, 380:** Theodosius I makes his adventus, or formal entry, into Constantinople. — [Theodosius I](https://en.wikipedia.org/wiki/Theodosius_I)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 7 followers

<!-- LATEST:END -->
