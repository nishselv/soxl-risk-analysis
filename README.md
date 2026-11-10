<div align="center">

# SOXL Risk Analysis

### Measuring downside risk in leveraged semiconductor ETFs

**Python · PostgreSQL · SQL · Statistics · Power BI**

*An end-to-end portfolio project evaluating whether semiconductor-market volatility can help identify periods of elevated downside risk in a 3× leveraged ETF.*

**Status:** In development · **Historical study period:** 2010–October 30, 2026

</div>

---

## Project overview

SOXL is a daily 3× leveraged semiconductor ETF. Its performance over several days depends not only on the direction of the semiconductor market but also on the path of returns, volatility, daily rebalancing, and fund costs. A period of heightened volatility can therefore create risks that are not obvious from a simple market-direction forecast.

This project asks:

> **Can historical semiconductor-volatility regimes identify periods when SOXL faces unusually high downside risk—and do they add predictive value beyond simpler approaches?**

The goal is **risk measurement and communication**, not a trading system. The final product is designed as a reproducible analysis and a two-page Power BI report that could help a brokerage risk team explain leveraged-ETF exposure and uncertainty.

## Questions the analysis will answer

1. How do SOXL's returns, drawdowns, and downside losses vary across historical volatility regimes?
2. Do regime-based estimates improve predictions of near-term losses compared with unconditional, continuous-volatility, and simple statistical baselines?
3. Are the findings stable under walk-forward testing and a separate, untouched 2026 holdout?
4. What can a semiconductor selloff reveal about the interaction of leverage, compounding, and volatility?

SOXL is the primary asset. SOXS is included for comparison, and SOXX / semiconductor-index data provide additional market context.

## Research design

| Component | Plan |
| --- | --- |
| Historical data | Daily market series beginning in 2010, with a fixed cutoff of **October 30, 2026** |
| Development period | **2010–2019** |
| Out-of-sample evaluation | **2020–2025**, using an expanding-window walk-forward design |
| Final holdout | **January–October 30, 2026**, evaluated separately after model choices are fixed |
| Primary risk horizons | **1-day and 5-day** downside outcomes |
| Supporting descriptions | **10-day and 20-day** risk summaries |
| Model comparisons | Unconditional rates, continuous-volatility measures, logistic/statistical baselines, and volatility-regime estimates |
| Evaluation | Calibration and Brier scores; VaR backtesting including Kupiec tests; bootstrap uncertainty with attention to overlapping outcomes |
| Case study | Decomposition of a 2026 semiconductor selloff and the effects of leverage and compounding |

**Avoiding look-ahead bias matters:** predictors must be observable at the time a forecast is made; regime thresholds and model parameters must be fitted only using the relevant training window. Negative or inconclusive results will be reported rather than hidden.

## Project workflow

```text
Market data sources
        │
        ▼
Python ingestion and validation
        │
        ▼
PostgreSQL storage + SQL transformations
        │
        ▼
Risk features and statistical baselines
        │
        ▼
Walk-forward evaluation + fixed 2026 holdout
        │
        ▼
Two-page Power BI risk report
        │
        ▼
Executive summary + documented limitations
```

## Deliverables and current progress

| Deliverable | Status |
| --- | --- |
| Local Python environment and initial repository setup | ✅ Complete |
| Initial SOXL, SOXS, and SOXX data retrieval checks | ✅ Working in initial test; **not yet validated** |
| FRED `NASDAQSOX` retrieval | ⚠️ Timed out; investigation pending |
| Data-quality checks and documented sources | 🔄 Initial checks exist; full validation pending |
| PostgreSQL tables and substantive SQL analysis | ⏳ Planned |
| Walk-forward risk models and uncertainty analysis | ⏳ Planned |
| 2026 holdout and selloff decomposition | ⏳ Planned |
| Automated tests and GitHub Actions | ⏳ Planned |
| **Exactly two** Power BI report pages | ⏳ Planned |
| Final findings, recommendations, and demonstration assets | ⏳ Planned |

### Results and dashboard

**Not available yet.** Quantitative findings, dashboard screenshots, SQL examples, and the final risk recommendation will be added only after the analysis has been completed and verified. This section will ultimately lead with the actual findings—not just the process.

## Data notes

- **SOXL, SOXS, SOXX:** initial daily-history retrieval uses `yfinance` (Yahoo Finance data). Split and distribution adjustments require verification before return calculations.
- **Semiconductor benchmark:** FRED's `NASDAQSOX` series represents the PHLX Semiconductor Sector Index. SOXL's benchmark changed in August 2021, so the FRED series must **not** be presented as its exact benchmark for the entire study period.
- **Reproducibility:** the ingestion script writes local raw-data snapshots and a `data/manifest.json` with source details and SHA-256 hashes. Raw data are excluded from Git; users retrieve their own copies under the applicable providers' terms.
- **Availability:** the current FRED request is unresolved. No fallback benchmark will be silently substituted.

Sources: [Direxion fund information](https://www.direxion.com/product/daily-semiconductor-bull-bear-3x-etfs) · [Direxion index-change notice](https://www.direxion.com/uploads/Direxion-Changes-Index-for-Semiconductor-ETFs.pdf) · [FRED NASDAQSOX](https://fred.stlouisfed.org/series/NASDAQSOX) · [yfinance documentation](https://ranaroussi.github.io/yfinance/reference/yfinance.price_history.html)

## Reproduce the initial data check

The commands below run the **current source-availability check**, not the eventual analysis pipeline. On macOS or Linux with Python 3.10+ installed:

```bash
git clone https://github.com/nishselv/soxl-risk-analysis.git
cd soxl-risk-analysis
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python check_data.py
```

The script attempts to download daily histories, reports coverage and duplicate/bad dates, and writes source snapshots to `data/raw/` plus a manifest to `data/manifest.json`. A source may fail independently; **check the terminal output and manifest errors before using any downloaded data**.

Once the SQL pipeline, tests, and reports are ready, this section will include full reproduction instructions.

## Technical stack

| Technology | Intended role |
| --- | --- |
| Python (`pandas`, `yfinance`, `requests`) | Acquisition, validation, feature engineering, and statistical analysis |
| PostgreSQL + SQL | Reproducible data organization and analytical queries |
| Power BI / DAX | Two-page interactive risk reporting |
| Git + GitHub Actions | Version control and automated testing |

## Documentation

- **[Development log](DEVELOPMENT_LOG.md)** — dated work journal, technical decisions, issues, fixes, and lessons learned.
- **Data-source methodology** — will be documented in `data_sources.md` as data validation progresses.
- **Model and dashboard documentation** — will be added alongside the corresponding completed work.

## Limitations and interpretation

SOXL and SOXS are daily leveraged products, not fixed-multiple long-horizon exposures. Historical market regimes may shift, adjusted-price histories can be revised, and a backtest can appear stronger than it is if thresholds, features, or comparisons inadvertently use future information. The final write-up will disclose these limitations and distinguish predictive results from descriptive observations.

*This is an educational research and portfolio project, not investment advice.*
