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
### 📅 Latest snapshot — 2026-08-02

> *"Yesterday is history, tomorrow is a mystery, today is God's gift, that's why we call it the present."* — **Joan Rivers**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $63,404 | +0.63% |
| Ethereum | $1,875.71 | +0.43% |
| Solana | $73.51 | +0.81% |

**🔭 NASA:** [A Fire Rainbow over West Virginia](https://apod.nasa.gov/apod/image/2608/FireRainbow_Harbig_960.jpg)

**🚗 Car news:** [All 20 BMW Art Cars Are Finally Together In One Place](https://www.motor1.com/news/803420/bmw-art-cars-welt/)

**📜 On this day, -338:** A Macedonian army led by Philip II defeated the combined forces of Athens and Thebes in the Battle of Chaeronea, securing Macedonian hegemony in Greece and the Aegean. — [Ancient Macedonian army](https://en.wikipedia.org/wiki/Ancient_Macedonian_army)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 7 repos · 0 followers

<!-- LATEST:END -->
