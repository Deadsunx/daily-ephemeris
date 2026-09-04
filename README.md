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
### 📅 Latest snapshot — 2026-09-04

> *"Do good by stealth, and blush to find it fame."* — **Alexander Pope**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $79,633 | -1.71% |
| Ethereum | $2,450.97 | -1.99% |
| Solana | $101.6 | -3.12% |

**🔭 NASA:** [Nā ʻUhane Māhoe Huki Pū i ke Ola](https://apod.nasa.gov/apod/image/2609/noirlab2621a_1024.jpg)

**🚗 Car news:** [The Dodge Durango Gets Darker For 2027 With New Paint](https://www.motor1.com/news/807196/2027-dodge-durango-new-paint/)

**📜 On this day, 476:** Romulus Augustulus is deposed when Odoacer proclaims himself "King of Italy", thus ending the Western Roman Empire. — [Romulus Augustulus](https://en.wikipedia.org/wiki/Romulus_Augustulus)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
