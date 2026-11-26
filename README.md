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
### 📅 Latest snapshot — 2026-11-26

> *"Keep your eyes on the stars, but remember to keep your feet on the ground."* — **Theodore Roosevelt**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $60,802 | +3.46% |
| Ethereum | $1,705.22 | +3.47% |
| Solana | $70.95 | +4.66% |

**🔭 NASA:** [NASA Science](https://science.nasa.gov/wp-content/themes/nasa-child/assets/images/nasa-logo@2x.png)

**🚗 Car news:** [2027 Toyota 4Runner Finally Adds Heated Seats, Then Crosses $45,000](https://www.motor1.com/news/816890/2027-toyota-4runner-price-updates/)

**📜 On this day, 783:** The Asturian queen Adosinda is held at a monastery to prevent her nephew from retaking the throne from Mauregatus. — [Kingdom of Asturias](https://en.wikipedia.org/wiki/Kingdom_of_Asturias)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 7 followers

<!-- LATEST:END -->
