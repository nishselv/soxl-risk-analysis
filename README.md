# SOXL Risk Analysis — Day 1 data availability check

**Purpose:** confirm which historical ETF and semiconductor benchmark series are retrievable and save source snapshots. **Not yet a validated backtesting dataset.**

## Run on macOS

1. Extract the `soxl-risk-day1.zip` archive in Downloads.
2. Open Terminal and run:

```bash
cd ~/Downloads/soxl-risk-day1
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python check_data.py
```

Python 3.10+ is recommended. If you extracted the archive somewhere else, adjust the `cd` path.

Files will appear in `data/raw/`, with source hashes and dates in `data/manifest.json`.

## Data notes

- SOXL and SOXS launched March 11, 2010.
- Direxion confirms a **benchmark switch around August 25, 2021** from PHLX Semiconductor Sector Index to ICE Semiconductor Index (currently described as NYSE Semiconductor Index; index identifier `ICESEMIT`).
- `NASDAQSOX` from FRED is a daily **PHLX SOX** series; it is useful for pre-switch comparisons and a *proxy* after the switch, not the fund's actual post-switch benchmark.
- Yahoo Finance price history is accessed through the unofficial `yfinance` Python library. It may fail, rate-limit, or revise historical adjusted prices. Keep the snapshots, report failures, and validate adjustments before any calculations.
- **Fixed final holdout cutoff:** October 30, 2026 inclusive. The code passes `end='2026-10-31'` because `yfinance` treats end as exclusive.
- `Adj Close` is the split-and-distribution-adjusted price series as provided by Yahoo, not a substitute for checking distributions and corporate actions.
- Avoid redistributing source market data unless permitted by its applicable licensing terms.

## Verified source links

- Direxion product: https://www.direxion.com/product/daily-semiconductor-bull-bear-3x-etfs
- 2021 index change: https://www.direxion.com/uploads/Direxion-Changes-Index-for-Semiconductor-ETFs.pdf
- FRED Nasdaq SOX series: https://fred.stlouisfed.org/series/NASDAQSOX
- yfinance API docs: https://ranaroussi.github.io/yfinance/reference/yfinance.price_history.html

## What to send back

Copy the Terminal output beginning with `Fetching SOXL` through `Sources downloaded`, or send a screenshot. If anything fails, share the exact error message.
