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
### 📅 Latest snapshot — 2026-09-22

> *"Every man's work, whether it be literature or music or pictures or architecture or anything else, is always a portrait of himself."* — **Samuel Butler**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $86,310 | +3.02% |
| Ethereum | $2,753.48 | +1.95% |
| Solana | $117.89 | +2.0% |

**🔭 NASA:** [Chance Triple Alignment: Plane, Space Station, Sun](https://apod.nasa.gov/apod/image/2609/PlaneIssSpots_Horalek_960.jpg)

**🚗 Car news:** [Volvo Already Has A New CEO, Just Two Years After Bringing Back Its Old One](https://www.motor1.com/news/809069/volvo-names-klaus-zellmer-next/)

**📜 On this day, 904:** The warlord Zhu Quanzhong kills Emperor Zhaozong, the penultimate emperor of the Tang dynasty, after seizing control of the imperial government. — [Zhu Wen](https://en.wikipedia.org/wiki/Zhu_Wen)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
