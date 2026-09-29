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
### 📅 Latest snapshot — 2026-09-29

> *"Silence is a source of great strength."* — **Lao Tzu**

**🔭 NASA:** [Sh2-188: The Shrimp Nebula](https://apod.nasa.gov/apod/image/2609/Shrimp_Pawel_960.jpg)

**🚗 Car news:** [BMW Tuner AC Schnitzer Gets A Second Chance After Nearly Shutting Down](https://www.motor1.com/news/810080/bmw-tuner-ac-schnitzer-new-owner/)

**📜 On this day, -61:** Pompey the Great celebrates his third triumph for victories over the pirates and the end of the Mithridatic Wars on his 45th birthday. — [Pompey](https://en.wikipedia.org/wiki/Pompey)

**🐙 GitHub [@Deadsunx](https://github.com/Deadsunx):** 11 repos · 9 followers

<!-- LATEST:END -->
