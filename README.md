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
### 📅 Latest snapshot — 2026-08-26

> *"A thing constructed can only be loved after it is constructed; but a thing created is loved before it exists."* — **Charles Dickens**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $77,899 | -1.74% |
| Ethereum | $2,439.79 | -1.49% |
| Solana | $95.55 | -2.98% |

**🔭 NASA:** [JWST Images The Lion's Head Nebula](https://apod.nasa.gov/apod/image/2608/lions_head_nebula.jpg)

**🚗 Car news:** [The Lincoln Corsair Returns For 2027 As A China-Built Hybrid](https://www.motor1.com/news/806182/2027-lincoln-corsair-hybrid-horsepower-trims-engine/)

**📜 On this day, 683:** The Battle of al-Harrah concludes, with Yazid I's army killing 11,000 people of the city of Medina. — [Battle of al-Harra](https://en.wikipedia.org/wiki/Battle_of_al-Harra)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 10 repos · 9 followers

<!-- LATEST:END -->
