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
### 📅 Latest snapshot — 2026-08-23

> *"The biggest adventure you can ever take is to live the life of your dreams."* — **Oprah Winfrey**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $77,260 | +0.15% |
| Ethereum | $2,444.25 | +1.06% |
| Solana | $95.28 | +1.55% |

**🔭 NASA:** [Cassini Approaches Saturn](https://player.vimeo.com/video/11386048#t=0m58s?color=8BA0FF&portrait=0)

**🚗 Car news:** [The Genesis G70 Is Losing Its Best Engine](https://www.motor1.com/news/805746/genesis-g70-v6-engine-discontinued/)

**📜 On this day, 79:** Mount Vesuvius begins stirring, on the feast day of Vulcan, the Roman god of fire. — [AD 79](https://en.wikipedia.org/wiki/AD_79)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 10 repos · 9 followers

<!-- LATEST:END -->
