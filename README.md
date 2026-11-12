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
### 📅 Latest snapshot — 2026-11-12

> *"In the practice of tolerance, one's enemy is the best teacher."* — **Dalai Lama**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $72,855 | -1.4% |
| Ethereum | $2,019.72 | -1.69% |
| Solana | $82.35 | -1.82% |

**🔭 NASA:** [NASA Science](https://science.nasa.gov/wp-content/themes/nasa-child/assets/images/nasa-logo@2x.png)

**🚗 Car news:** [Scout Is Finally Building Real Vehicles At Its $2-Billion Factory](https://www.motor1.com/news/815073/scout-builds-terra-traveler-prototypes-factory/)

**📜 On this day, 954:** The 13-year-old Lothair III is crowned at the Abbey of Saint-Remi as king of the West Frankish Kingdom. — [Lothair of France](https://en.wikipedia.org/wiki/Lothair_of_France)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
