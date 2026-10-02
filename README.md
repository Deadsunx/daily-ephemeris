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
### 📅 Latest snapshot — 2026-10-02

> *"I learned that courage was not the absence of fear, but the triumph over it. The brave man is not he who does not feel afraid, but he who conquers that fear."* — **Nelson Mandela**

**Crypto (USD)**

| Coin | Price | 24h |
| --- | --- | --- |
| Bitcoin | $84,370 | -0.48% |
| Ethereum | $2,667.88 | -1.3% |
| Solana | $118.03 | -0.28% |

**🚗 Car news:** [BMW Celebrates One Million M Cars By Teasing The Next M3](https://www.motor1.com/news/810652/bmw-m-1-million-milestone/)

**📜 On this day, -48:** Julius Caesar arrives in Ptolemaic Egypt in his pursuit of Pompey and learns of the latter's death. — [Julius Caesar](https://en.wikipedia.org/wiki/Julius_Caesar)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 10 followers

<!-- LATEST:END -->
