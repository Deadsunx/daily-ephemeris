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
### 📅 Latest snapshot — 2026-11-02

> *"If you want others to be happy, practice compassion. If you want to be happy, practice compassion."* — **Dalai Lama**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $77,758 | -0.13% |
| Ethereum | $2,282.73 | +0.62% |
| Solana | $93.85 | -1.45% |

**🚗 Car news:** [Ferrari Challenge Stradale Is Reportedly Returning After 20-Plus Years](https://www.autoblog.com/news/ferrari-challenge-stradale-is-reportedly-returning-after-20-plus-years)

**📜 On this day, 619:** A qaghan of the Western Turkic Khaganate is assassinated in a Chinese palace by Eastern Turkic rivals after the approval of Tang emperor Gaozu. — [Great Khan](https://en.wikipedia.org/wiki/Great_Khan)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 10 followers

<!-- LATEST:END -->
