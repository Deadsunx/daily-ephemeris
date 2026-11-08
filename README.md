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
### 📅 Latest snapshot — 2026-11-08

> *"People spend too much time doing and not enough time thinking about what they should be doing."* — **Naval Ravikant**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $75,810 | -0.12% |
| Ethereum | $2,233.57 | -0.43% |
| Solana | $89.13 | -0.78% |

**🚗 Car news:** [BYD's New Flagship Sedan Wants To Be China's Most Luxurious Car Yet](https://www.motor1.com/news/814760/byd-yangwang-altior-revealed/)

**📜 On this day, 960:** Battle of Andrassos: Byzantines under Leo Phokas the Younger score a crushing victory over the Hamdanid Emir of Aleppo, Sayf al-Dawla. — [Battle of Andrassos](https://en.wikipedia.org/wiki/Battle_of_Andrassos)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
