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
### 📅 Latest snapshot — 2026-08-30

> *"Keep your eyes on the goal, and just keep taking the next step towards completing it."* — **John Carmack**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $79,022 | +1.11% |
| Ethereum | $2,510.19 | +2.35% |
| Solana | $106.68 | +1.45% |

**🔭 NASA:** [M74: A Grand Design Spiral](https://apod.nasa.gov/apod/image/2608/m74_hst_960.jpg)

**🚗 Car news:** [Maserati's Origin Story Gets The Hollywood Treatment With New Movie: Watch The Trailer](https://www.motor1.com/news/806439/new-maserati-movie-pacino-hopkins/)

**📜 On this day, 70:** Titus ends the siege of Jerusalem after destroying Herod's Temple. — [AD 70](https://en.wikipedia.org/wiki/AD_70)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 10 repos · 9 followers

<!-- LATEST:END -->
