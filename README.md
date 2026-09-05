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
### 📅 Latest snapshot — 2026-09-05

> *"However difficult life may seem, there is always something you can do and succeed at."* — **Stephen Hawking**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $79,736 | -1.16% |
| Ethereum | $2,457.78 | -1.86% |
| Solana | $102.22 | -1.32% |

**🔭 NASA:** [Chasing the Moon's Shadow](https://apod.nasa.gov/apod/image/2609/2026Eclipse_WB57GoPro_Totality_H264_1024.jpg)

**🚗 Car news:** [The Dodge Durango Gets Darker For 2027 With New Paint](https://www.motor1.com/news/807196/2027-dodge-durango-new-paint/)

**📜 On this day, 394:** On the first day of the battle of Frigidus, the Western Roman troops of Arbogast manage to defend their positions against the Eastern Roman troops of emperor Theodosius I. — [Battle of the Frigidus](https://en.wikipedia.org/wiki/Battle_of_the_Frigidus)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
