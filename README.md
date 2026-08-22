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
### 📅 Latest snapshot — 2026-08-22

> *"Our virtues and our failings are inseparable, like force and matter. When they separate, man is no more."* — **Nikola Tesla**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $78,424 | +4.75% |
| Ethereum | $2,512.01 | +7.0% |
| Solana | $97.13 | +8.88% |

**🔭 NASA:** [Mostly Perseids](https://apod.nasa.gov/apod/image/2608/allsky_CEMeNt_Aug12-13final_pretty_8bit1024.jpg)

**🚗 Car news:** [Is Ford Considering A Cheap Rally Car? Sure Sounds Like It](https://www.motor1.com/news/805740/affordable-ford-rally-car-jim-farley-rumor/)

**📜 On this day, 392:** Arbogast has Eugenius elected Western Roman Emperor. — [Arbogast (magister militum)](https://en.wikipedia.org/wiki/Arbogast_(magister_militum))

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 10 repos · 8 followers

<!-- LATEST:END -->
