<h1 align="center">SOXL Risk Analysis</h1>

<p align="center"><strong>Forecasting downside risk in daily leveraged semiconductor ETFs</strong></p>

<p align="center"><strong>Python · Jupyter · PostgreSQL · SQL · Statistical modelling · Power BI</strong></p>

<p align="center"><em>Version 2.2 · Historical cutoff: October 30, 2026 · Research and portfolio project</em></p>

> **Current milestone — Stage 1.2:** Five-source data validation, the isolated fresh-download test, and the complete clean-kernel notebook execution passed on November 9, 2026. The final data-quality assessment is complete. Final documentation/source-rights review and GitHub publication remain open. **The expanded notebook and latest changes have not yet been verified as pushed.**

[Research question](#research-question) · [Study design](#study-design) · [Project stages](#project-stage-checklists) · [Verified findings](#verified-data-validation-findings) · [Reproduce](#reproduce-the-data-check) · [Development log](DEVELOPMENT_LOG.md)

---

## Research question

**Can recent semiconductor-market conditions—including realized volatility and broader market-implied volatility (VIX)—help estimate when SOXL is more likely to experience a significant near-term loss?**

[SOXL](https://www.direxion.com/product/daily-semiconductor-bull-bear-3x-etfs) targets **3× the daily** performance of a semiconductor index, before fees and expenses. Its multi-day outcome can diverge from three times the index's multi-day return due to daily compounding and volatility. SOXS is included as an inverse-leveraged comparator, SOXX as an unleveraged semiconductor ETF, and VIX as a broader market-risk indicator.

The project measures and tests *downside risk* rather than generating trades or predicting exact prices. One practical example is the probability of a SOXL loss of at least 10% over the next five trading days; thresholds and forecasting conventions will be specified and frozen during modelling.

## Study design

| Design choice | Plan |
|---|---|
| Data range | March 2010–October 30, 2026 |
| Initial development | 2010–2019 |
| Walk-forward testing | 2020–2025, expanding training windows |
| Final holdout | January–October 30, 2026; reserved for evaluation after model decisions are locked |
| Primary targets | 1-day and 5-day SOXL downside outcomes |
| Supporting views | 10-day and 20-day risk summaries; drawdowns and leverage/compounding |
| Candidate context | SOXX and `NASDAQSOX` sector history; VIX (`VIXCLS`); trailing realized volatility |
| Planned comparisons | Unconditional and continuous-volatility baselines, simple statistical models, and volatility regimes; with/without VIX |
| Planned evaluation | Calibration, Brier scores, VaR exceedances/Kupiec tests, appropriate bootstrap uncertainty |
| Final presentation | **Exactly two Power BI report pages**, with an executive summary and reproducibility notes |

**Leakage policy:** Forecast features must have been available at the forecast time; threshold selection, transformations, and fitting belong inside the appropriate training window. The 2026 holdout must not be used to select models. A completed 2026 data-quality audit is not permission to tune on 2026 outcomes.

## Data and workflow

| Data | Source | Intended role | Important note |
|---|---|---|---|
| SOXL | Yahoo Finance via `yfinance` | Primary 3× long risk asset | Returns from `Adj Close`, subject to source limitations |
| SOXS | Yahoo Finance via `yfinance` | Inverse-leveraged comparator | Early historical volume is unreliable |
| SOXX | Yahoo Finance via `yfinance` | Unleveraged sector reference | Pre-Oct. 15, 2010 history is predecessor IGW history |
| `NASDAQSOX` | FRED | Historical PHLX reference / sector proxy | **Not** the exact leveraged-fund benchmark from Aug. 25, 2021 onward |
| `VIXCLS` | FRED (Cboe) | Broad-market options-implied volatility | Not semiconductor-specific |

Cboe's published VIX history is retained as a **reference** for cross-checking `VIXCLS`, not counted as a sixth primary modelling dataset. Original source CSVs are local and excluded from Git; their SHA-256 hashes are tracked in `data/manifest.json`, which is also stored locally and excluded from Git.

```text
Original market data + Cboe reference
                   |
                   v
Python ingestion -> Notebook 01: source validation
                   |
                   v
Notebook 02: exploratory market analysis
                   |
                   v
PostgreSQL + SQL: repeatable transformations
                   |
                   v
Notebook 03: risk metrics and historical features
                   |
                   v
Notebook 04: baselines, volatility regimes and VIX tests
                   |
                   v
Notebook 05: expanding-window evaluation (2020-2025)
                   |
                   v
Frozen 2026 holdout + semiconductor selloff case study
                   |
                   v
Two-page Power BI report + portfolio findings
```

## Project stage checklists

**How to read this:** `[x]` means the work has been performed and reviewed; `[ ]` means still open. The **same milestone lines** appear at the beginning of each stage in [DEVELOPMENT_LOG.md](DEVELOPMENT_LOG.md), followed there by detailed tasks and dated work notes. A notebook is not considered a *published* milestone until its GitHub push has been verified.

### Stage 1.1 — Project Foundation and Data Acquisition

**Status:** Foundation operational. [Detailed stage log](DEVELOPMENT_LOG.md#phase-11--project-foundation-and-data-acquisition).

- [x] Define Version 2.2 research scope, historical cutoff, and evaluation periods.
- [x] Set up the Python environment, Git repository, and project documentation.
- [x] Collect and preserve the five primary market-data snapshots and Cboe VIX reference.
- [x] Maintain protected raw files and a checksum-based source manifest.

### Stage 1.2 — Data Quality Validation

**Status:** Analytical validation and reproducibility passed locally; final documentation review and GitHub publication pending. **Evidence:** [`01_data_validation.ipynb`](notebooks/01_data_validation.ipynb) (full five-source clean-kernel run passed November 9, 2026; latest version not yet GitHub-verified). [Detailed stage log](DEVELOPMENT_LOG.md#phase-12--data-quality-validation).

- [x] Validate ETF prices, calendars, corporate actions, extreme returns, and volume anomalies.
- [x] Check benchmark history and validate VIX against Cboe reference data.
- [x] Record five-source provenance, restrictions, and methodology in Notebook 01.
- [x] Verify fresh five-source downloads in isolation and rerun Notebook 01 from a clean kernel.
- [ ] Review source rights, dependencies, and documentation; commit and verify the GitHub milestone.

### Stage 2 — Exploratory Analysis

**Status:** Planned. **Planned notebook:** `02_exploratory_analysis.ipynb`. [Detailed stage log](DEVELOPMENT_LOG.md#phase-2--exploratory-analysis).

- [ ] Build date-aligned ETF return and volatility comparisons in Notebook 02.
- [ ] Explore drawdowns, leverage effects, semiconductor conditions, and VIX relationships.
- [ ] Document useful visuals and observations without tuning on the 2026 holdout.
- [ ] Validate, document, commit, and publish Notebook 02.

### Stage 3 — PostgreSQL and SQL

**Status:** Planned. [Detailed stage log](DEVELOPMENT_LOG.md#phase-3--postgresql-and-sql).

- [ ] Design PostgreSQL tables for sources, trading dates, returns, and metadata.
- [ ] Create reproducible data imports and date-safe SQL transformations.
- [ ] Compare SQL calculations with independently checked Python outputs.
- [ ] Document schema, queries, tests, and the completed SQL milestone.

### Stage 4 — Risk Metrics and Feature Engineering

**Status:** Planned. **Planned notebook:** `03_risk_metrics.ipynb`. [Detailed stage log](DEVELOPMENT_LOG.md#phase-4--risk-metrics-and-feature-engineering).

- [ ] Define 1-day and 5-day downside outcomes and 10-day/20-day supporting summaries.
- [ ] Calculate downside frequencies, drawdowns, VaR, and other descriptive risk measures in Notebook 03.
- [ ] Build past-only return, realized-volatility, regime, and VIX features.
- [ ] Test data leakage and document the reproducible feature set.

### Stage 5 — Volatility Modelling

**Status:** Planned. **Planned notebook:** `04_volatility_modeling.ipynb`. [Detailed stage log](DEVELOPMENT_LOG.md#phase-5--volatility-modelling).

- [ ] Fit unconditional, simple statistical, and volatility-regime risk baselines in Notebook 04.
- [ ] Evaluate whether adding VIX improves risk estimates beyond semiconductor features.
- [ ] Fit preprocessing and regime boundaries using training data only.
- [ ] Document assumptions, comparisons, and a versioned modelling milestone.

### Stage 6 — Walk-Forward Evaluation

**Status:** Planned. **Planned notebook:** `05_backtesting.ipynb`. [Detailed stage log](DEVELOPMENT_LOG.md#phase-6--walk-forward-evaluation).

- [ ] Run expanding-window out-of-sample evaluation across 2020–2025 in Notebook 05.
- [ ] Assess calibration, Brier scores, VaR/Kupiec tests, and uncertainty.
- [ ] Account for overlapping forecast horizons and record negative results.
- [ ] Freeze the final modelling decisions before opening the 2026 holdout.

### Stage 7 — 2026 Holdout and Case Study

**Status:** Planned. [Detailed stage log](DEVELOPMENT_LOG.md#phase-7--2026-holdout-and-case-study).

- [ ] Evaluate the frozen approach once on the January–October 2026 holdout.
- [ ] Investigate a 2026 semiconductor selloff and leverage/compounding effects.
- [ ] Present holdout performance, uncertainty, benchmark caveats, and limitations.
- [ ] Commit a reproducible holdout and case-study milestone.

### Stage 8 — Power BI and Final Portfolio Release

**Status:** Planned. [Detailed stage log](DEVELOPMENT_LOG.md#phase-8--power-bi-and-final-portfolio-release).

- [ ] Build exactly two Power BI pages for risk monitoring and model evaluation.
- [ ] Write the executive summary, key findings, and responsible interpretation.
- [ ] Publish reproducibility instructions, representative visuals, and portfolio walkthrough.
- [ ] Complete appropriate automated checks and verify the final GitHub release.

## Verified data-validation findings

*The results below were validated locally in Notebook 01. The five-source collection script passed the isolated fresh-download test, and the revised notebook ran successfully from a clean kernel. Publication of these latest changes to GitHub has not yet been verified.*

| Finding | Local validation result |
|---|---|
| Shared ETF calendar | **4,187** dates, March 11, 2010–October 30, 2026 |
| SOXX / valid `NASDAQSOX` calendar | **4,195** matching dates; the original FRED file includes **155** non-observed days |
| Stock splits | **13 / 13** dates and ratios match reference records (**6** labelled primary-source, **7** secondary-source) |
| Adjusted-price returns | Internally consistent with the tested dividend-adjustment convention; not independent price authentication |
| SOXS volume anomaly | **1,986** zero-volume observations, **1,976** with changing closing prices; early volume restricted |
| VIXCLS | **4,350** FRED rows, **122** missing values; valid on all **4,187** common ETF dates |
| VIX versus Cboe | **0.00** maximum closing-level difference across the common ETF dates |
| Source provenance | **5 / 5** primary-file hashes match manifest; Cboe reference preserved |
| Collection reproducibility | All **5** primary sources downloaded in isolation, **0** errors; original source snapshots unchanged |
| Notebook reproducibility | Complete revised Notebook 01 executed successfully from a fresh kernel |

**Assessment:** Conditionally suitable for downstream risk analysis, with documented historical-volume, benchmark, provider, and licensing caveats. Cross-provider agreement for VIX is not independent verification of its underlying index calculation because FRED republishes Cboe data.

**Notebook:** [`notebooks/01_data_validation.ipynb`](notebooks/01_data_validation.ipynb) · **Supporting collection script:** [`check_data.py`](check_data.py) · **Full evidence:** [`DEVELOPMENT_LOG.md`](DEVELOPMENT_LOG.md#phase-12--data-quality-validation).

## Results and dashboard

**Predictive modelling and dashboard results are not yet available.** Predictive accuracy, risk-calibration findings, holdout results, screenshots, and the final interpretation will be added only after the relevant stages are completed and verified. Negative or inconclusive results will be reported.

## Reproduce the data check

These commands set up the initial data-collection and notebook workflow, **not** a completed predictive risk-model pipeline. They require a compatible Python version and access to the applicable data providers.

```bash
git clone https://github.com/nishselv/soxl-risk-analysis.git
cd soxl-risk-analysis
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python check_data.py
jupyter lab
```

Open [`notebooks/01_data_validation.ipynb`](notebooks/01_data_validation.ipynb) in JupyterLab, use the project root as the working directory, and run cells in order. The original validated source snapshots are **not** included in Git: `check_data.py` downloads missing primary files and reuses existing ones. Notebook 01 also retrieves or reuses the separate Cboe VIX reference for cross-provider validation. Review the manifest, errors, and notebook checks rather than assuming every provider request succeeded.

The updated collection script successfully downloaded all five primary datasets in an isolated, empty temporary directory without changing the original validated snapshots. The full notebook also ran from a fresh kernel in the project's existing environment. **Installation and end-to-end notebook execution in an entirely new environment have not been independently tested.** Fresh downloads may differ from the preserved validated files if providers revise historical data.

Source files are intentionally excluded from GitHub. Financial-provider data may be revised and may have separate use or redistribution restrictions. Source rights and historical benchmark definitions require care before redistributing raw prices.

## Repository guide

| Path | Purpose |
|---|---|
| [`notebooks/01_data_validation.ipynb`](notebooks/01_data_validation.ipynb) | Five-source data validation, findings, and limitations |
| [`check_data.py`](check_data.py) | Local collection and snapshot-protection script |
| [`DEVELOPMENT_LOG.md`](DEVELOPMENT_LOG.md) | **Matching stage checklists**, detailed steps, dated evidence, and decisions |
| `requirements.txt` | Reviewed Python dependencies: pandas, yfinance, requests, JupyterLab, ipykernel, and Matplotlib |
| `data/raw/` *(local, ignored)* | Preserved source snapshots |
| `data/manifest.json` *(local, ignored)* | Source identities and SHA-256 fingerprints |
| `data_sources.md` *(planned)* | Source definitions, benchmark chronology, licensing, and update guidance |

## Limitations and responsible interpretation

Daily leveraged ETFs are not fixed-multiple long-horizon exposures. Data can be revised; historical benchmarks have changed; early SOXS volume is unreliable; VIX is broad-market implied volatility rather than a semiconductor risk forecast; and risk models can overfit unless evaluated in strictly chronological windows. Not every ETF price or distribution has been independently confirmed, and some split records rely on secondary references. Source licensing and redistribution rights remain under review. This is an educational analytical project and **not investment advice**.

**Source context:** [Direxion](https://www.direxion.com/product/daily-semiconductor-bull-bear-3x-etfs) · [FRED `NASDAQSOX`](https://fred.stlouisfed.org/series/NASDAQSOX) · [FRED `VIXCLS`](https://fred.stlouisfed.org/series/VIXCLS) · [Cboe VIX historical data](https://www.cboe.com/tradable-products/vix/vix-historical-data) · [yfinance documentation](https://ranaroussi.github.io/yfinance/)
