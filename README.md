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
### 📅 Latest snapshot — 2026-09-25

> *"Give so much away people insist on paying you."* — **Jack Butcher**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $84,029 | -0.48% |
| Ethereum | $2,694.72 | -0.08% |
| Solana | $121.91 | +3.85% |

**🔭 NASA:** [Globular Cluster Omega Centauri](https://apod.nasa.gov/apod/image/2609/NGC5139CadenasParra1024.jpg)

**🚗 Car news:** [Listen To The 960-HP Jensen Interceptor Unleash Its Supercharged V8](https://www.motor1.com/news/809644/jensen-interceptor-gtx-engine-sound/)

**📜 On this day, 275:** For the last time, the Roman Senate chooses an emperor; they elect 75-year-old Marcus Claudius Tacitus. — [Tacitus (emperor)](https://en.wikipedia.org/wiki/Tacitus_(emperor))

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
