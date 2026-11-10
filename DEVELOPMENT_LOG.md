# Development Log — SOXL Risk Analysis

*A chronological record of implementation, analysis, decisions, troubleshooting, and lessons learned for Version 2.2.*

**Repository:** [nishselv/soxl-risk-analysis](https://github.com/nishselv/soxl-risk-analysis)\
**Portfolio overview:** [README.md](README.md)\
**Primary analysis notebook:** [notebooks/01_data_validation.ipynb](notebooks/01_data_validation.ipynb)\
**Historical data cutoff:** October 30, 2026\
**Last documented session:** November 9, 2026\
**Current phase:** 1.2 — Data Quality Validation (**analytical work completed; final publication checks pending**)\
**Last confirmed GitHub commit:** `0e2c805` — `Add Jupyter notebook for data quality validation`

> **Synchronization note (November 9, 2026):** The last verified GitHub commit remains `0e2c805`. The expanded five-source notebook, revised collection script, and latest documentation are completed **locally but not yet confirmed pushed**. The isolated fresh-download test and complete five-source fresh-kernel notebook run **both passed** on November 9, 2026. README and development-log checklists have been reviewed and synchronized. Final source-rights review, Git inspection, and verified publication remain pending.

---

## How this log is maintained

The `README.md` is the concise, public-facing project overview. This document is the detailed record of *how* the project is being built.

For every meaningful work session, record the objective, work completed, actual results, errors and attempted fixes, methodology decisions, concepts learned, open limitations, and next actions. A failed attempt remains in the history even after it is fixed.

### Phase tracking rules

1. Start each new phase with its **objective**, **scope**, and a **progress checklist** immediately below the introduction.
2. Mark an item `[x]` only after the relevant work has been performed and its outcome reviewed. An initial screening is not the same as independent source verification.
3. Update the checklist and add the relevant dated log entry whenever a milestone is completed.
4. Save the notebook and this log together. At meaningful milestones, commit and push both to GitHub; confirm the actual push before describing work as published.
5. At phase completion, run the full notebook from top to bottom, record final conclusions and unresolved limitations, update the README, and verify the GitHub commit before beginning the next notebook.
6. For **every phase**, keep the **Stage milestones — mirrored in README** checklist identical (same wording and checked state) in both files. Under it, maintain a more granular **Detailed work checklist** and all dated work notes for that phase. Review the two files together before pushing.

### Working tools and responsibilities

| Tool or file | Responsibility |
|---|---|
| **JupyterLab notebooks** | Main workspace for exploratory Python code, validation, calculations, output tables, meaningful diagnostic charts, and written interpretations |
| **Standalone Python scripts** | Reusable operations such as downloading and processing datasets; these can be edited in JupyterLab |
| **Terminal** | Supporting tasks: environment setup, dependency installation, running Git commands, and troubleshooting |
| **Git/GitHub** | Version control and published milestones; local notebook changes do **not** push automatically |
| **`README.md`** | Short, professional overview, methodology, verified results, and project status |
| **`DEVELOPMENT_LOG.md`** | Chronological reasoning, evidence, issues, decisions, and phase checklist |

**Notebook policy:** One notebook has one primary purpose. Only move to the next notebook after the current one's scope has been completed and documented. Add visualizations when they help test an assumption, diagnose data, or communicate a result—not merely to decorate the notebook.

---

## Stage overview

| Stage | Main deliverable | Current status |
|---|---|---|
| [1.1 — Project Foundation and Data Acquisition](#phase-11--project-foundation-and-data-acquisition) | Source snapshots + collection script | Foundation operational |
| [1.2 — Data Quality Validation](#phase-12--data-quality-validation) | [Notebook 01](notebooks/01_data_validation.ipynb) | In final review |
| [2 — Exploratory Analysis](#phase-2--exploratory-analysis) | `02_exploratory_analysis.ipynb` | Planned |
| [3 — PostgreSQL and SQL](#phase-3--postgresql-and-sql) | PostgreSQL schema + SQL queries | Planned |
| [4 — Risk Metrics and Feature Engineering](#phase-4--risk-metrics-and-feature-engineering) | `03_risk_metrics.ipynb` | Planned |
| [5 — Volatility Modelling](#phase-5--volatility-modelling) | `04_volatility_modeling.ipynb` | Planned |
| [6 — Walk-Forward Evaluation](#phase-6--walk-forward-evaluation) | `05_backtesting.ipynb` | Planned |
| [7 — 2026 Holdout and Case Study](#phase-7--2026-holdout-and-case-study) | 2026 holdout + selloff case study | Planned |
| [8 — Power BI and Final Portfolio Release](#phase-8--power-bi-and-final-portfolio-release) | Two-page Power BI report + portfolio | Planned |

**Evidence standard:** A completed local analysis is not a published GitHub milestone until its output, documentation, and commit are verified.

---

## Phase 1.1 — Project Foundation and Data Acquisition

### Objective and scope

Set up a reproducible macOS/Python project, publish the initial repository, and retrieve historical daily market data needed for a leveraged-semiconductor-ETF downside-risk study.

### Stage milestones — mirrored in README

- [x] Define Version 2.2 research scope, historical cutoff, and evaluation periods.
- [x] Set up the Python environment, Git repository, and project documentation.
- [x] Collect and preserve the five primary market-data snapshots and Cboe VIX reference.
- [x] Maintain protected raw files and a checksum-based source manifest.

These milestone checkboxes are intentionally identical to the README. The more detailed task list below records the evidence and smaller steps.

### Detailed work checklist (evidence and next actions)

- [x] Freeze the Version 2.2 project scope and historical cutoff.
- [x] Create the local project and Python virtual environment.
- [x] Install the initial Python dependencies.
- [x] Build `check_data.py` and a source manifest.
- [x] Create `.gitignore`, README, and development log.
- [x] Initialize Git, connect GitHub, and publish the initial commits.
- [x] Resolve the observed FRED download timeout and retrieve all four datasets.
- [ ] Finish source-definition and licensing review for all five primary datasets and the Cboe reference. *Benchmark chronology researched and documented in Phase 1.2; final licensing/exact-index-source review remains open.*
- [x] Remove the deprecated `raise_errors` argument from `check_data.py` and verify the revised download path. *The isolated fresh-download test succeeded without that warning in the reported output.*

**Phase status:** Repository foundation and five-source collection workflow are operational. Both existing-file reuse and isolated fresh-download tests passed. Exact replacement-benchmark sourcing and redistribution/licensing review remain open as documented external limitations.

### November 9, 2026 — Establishing the project

**Objective:** Create the foundation for a Python, PostgreSQL/SQL, statistics, and Power BI portfolio project measuring SOXL downside risk.

**Work completed:**

- Established Version 2.2. SOXL is the primary risk asset, SOXS is a leveraged-inverse comparator, and SOXX plus semiconductor-index data provide market context.
- Fixed the historical cutoff at **October 30, 2026**. Planned development period: **2010–2019**; expanding-window out-of-sample evaluation: **2020–2025**; untouched final holdout: **January–October 30, 2026**.
- Defined primary **1-day and 5-day** downside outcomes, with **10-day and 20-day** supporting summaries. Planned comparisons include unconditional estimates, volatility-based features, simple statistical baselines, and volatility-regime models.
- Defined later evaluation work: calibration, Brier scores, Value at Risk (VaR) backtesting, Kupiec tests, uncertainty analysis, and a 2026 selloff case study. The final Power BI report will have **exactly two pages**.
- Created `~/Downloads/Personal Project - SOXL` and a Python **3.14.7** virtual environment named `.venv`.
- Installed `pandas`, `yfinance`, `requests`, and supporting dependencies.
- Created `check_data.py`. It downloads ETF price histories through `yfinance` and the `NASDAQSOX` series from FRED through `requests`, writes local CSV source snapshots, and produces `data/manifest.json` with retrieval information and checksums.
- Created `.gitignore` to exclude `.venv`, downloaded `data/` content, temporary files, and ZIP archives. The raw financial datasets remain local rather than being published on GitHub.

**What I learned:** A reproducible project needs explicit assumptions, a fixed data cutoff, a record of data provenance, and a distinction between *data downloaded* and *data validated*. The project is a risk-analysis study, not a trading signal or investment recommendation.

### November 9, 2026 — Initial GitHub publication and documentation structure

**Objective:** Version the project and distinguish public-facing documentation from the detailed engineering journal.

| Commit | Verified description |
|---|---|
| `ff44a57` | `Initial setup: SOXL Risk Analysis Project` — initial `.gitignore`, README, download script, and requirements |
| `ec525ca` | `Docs: Redesign README and add development log` — polished README and new `DEVELOPMENT_LOG.md` |
| `26965b5` | `Fix FRED data download and document resolution` — date-bounded FRED request and documented fix |
| `0e2c805` | `Add Jupyter notebook for data quality validation` — first notebook, Jupyter dependencies, and log update |

**Verification:** Connected `origin` to `https://github.com/nishselv/soxl-risk-analysis.git` and confirmed successful pushes to the `main` branch. The latest *confirmed* published commit is `0e2c805`.

**Decision:** `README.md` will present the research problem, methodology, progress, and verified outputs. `DEVELOPMENT_LOG.md` will retain technical decisions, failed attempts, troubleshooting, and explanations of new concepts. Source details and licensing limitations will eventually be consolidated in `data_sources.md`.

### Issue 001 — FRED CSV request timed out

**Status:** **Resolved for retrieval on November 9, 2026.** Exact original cause not established.

**Observed problem:** SOXL, SOXS, and SOXX downloaded, but the original FRED request repeatedly timed out after a 40-second read timeout.

**Why it mattered:** The missing index series prevented completion of the intended source-collection step. Silently replacing it would make later benchmark comparisons difficult to interpret.

**Investigation and attempted fixes:**

1. Tested a date-bounded FRED CSV URL using `curl`: HTTP **200**, **79,937 bytes**, approximately **1.31 seconds**.
2. Checked the first and last observations: **March 1, 2010** through **October 30, 2026**.
3. Repeated the bounded URL test using Python `requests`: HTTP **200**, **79,937 bytes**.
4. Updated `check_data.py` to request the explicit period and use separate connection/read timeouts of **10/20 seconds**.
5. Reran the entire retrieval script successfully.

**Verified result:** `Sources downloaded: 4 | Issues: 0`. The FRED file contained **4,350 rows**, with no duplicate or invalid dates.

**What I learned:** **FRED** means *Federal Reserve Economic Data*, a database maintained by the Federal Reserve Bank of St. Louis. `NASDAQSOX` provides historical PHLX Semiconductor Sector Index data. It is not SOXL's exact benchmark over the entire study: the fund changed benchmarks in August 2021. The specific cause of the initial timeout remains uncertain; the modified request simply resolved the observed failure.

**Follow-up status (updated November 9):** Benchmark change dates and the appropriate pre-/post-August-2021 interpretation were documented in Notebook 01. Actual ICE/NYSE index sourcing and relevant licensing/redistribution permissions remain open; do not present NASDAQSOX as the exact post-2021 leveraged-fund benchmark.

### Issue 002 — `yfinance` deprecation warning

**Status:** **Resolved for the observed `raise_errors` warning on November 9, 2026.** The original script emitted a non-blocking deprecation warning. The revised `check_data.py` no longer passes `raise_errors`; the isolated fresh-download test retrieved all three Yahoo ETF series successfully and the reported output did not show the previous warning. Other future provider/API warnings remain possible.

---

## Phase 1.2 — Data Quality Validation

### Objective and scope

Confirm that the **five primary series**—SOXL, SOXS, SOXX, `NASDAQSOX`, and `VIXCLS`—are sufficiently complete, aligned, and suitable for responsible downside-risk analysis. Cboe historical VIX prices serve as an additional source-reference dataset. The primary deliverable is **`notebooks/01_data_validation.ipynb`**, containing reproducible tests, output tables, carefully chosen diagnostic plots, methodology decisions, and a five-source final assessment.

Original source CSVs remain unchanged. Screens and exploratory tests in Terminal are retained as historical evidence but must be reproduced in the notebook where appropriate before this phase is considered complete.

### Stage milestones — mirrored in README

- [x] Validate ETF prices, calendars, corporate actions, extreme returns, and volume anomalies.
- [x] Check benchmark history and validate VIX against Cboe reference data.
- [x] Record five-source provenance, restrictions, and methodology in Notebook 01.
- [x] Verify fresh five-source downloads in isolation and rerun Notebook 01 from a clean kernel.
- [ ] Review source rights, dependencies, and documentation; commit and verify the GitHub milestone.

These milestone checkboxes are intentionally identical to the README. The more detailed task list below records the evidence and smaller steps.

### Detailed work checklist (evidence and next actions)

#### Source acquisition, notebook setup, and trading calendars

- [x] Retrieve the original SOXL, SOXS, SOXX, and NASDAQSOX data.
- [x] Add historical VIX (`VIXCLS`) as the fifth primary source; retain Cboe's reference VIX history separately.
- [x] Install JupyterLab/`ipykernel` and create `notebooks/01_data_validation.ipynb`.
- [x] Commit and push the *initial* notebook and supporting files (`0e2c805`).
- [x] Reproduce missing-value, invalid-date, duplicate-date, and ETF trading-calendar checks in Jupyter.
- [x] Explain 155 NASDAQSOX non-observations by verifying that 4,195 valid dates match SOXX dates.
- [x] Confirm the 4,187-date common SOXL/SOXS/SOXX calendar.
- [x] Check nonpositive prices, OHLC price relationships, and negative/missing ETF volume.
- [x] Generate original-source SHA-256 checksums and a consolidated five-source inventory.

#### Corporate actions, unusual observations, and source definitions

- [x] Identify 13 ETF split records and check split-day price-return consistency.
- [x] Cross-check all 13 split dates and ratios with a reference table (six primary-source and seven secondary-source matches).
- [x] Examine dividend counts, the large historically split-adjusted SOXS distributions, and their cumulative split factors.
- [x] Compare simple cash-distribution returns with the adjustment convention implied by Yahoo's adjusted prices.
- [x] Reproduce extreme-return screening and investigate selected dates using SOXX/FRED sector comparisons.
- [x] Produce a cross-ETF extreme-date chart and an annual SOXS zero-volume diagnostic chart.
- [x] Document the benchmark regimes, NASDAQSOX's pre-/post-2021 role, and the predecessor IGW history for SOXX.
- [x] Investigate SOXS's 1,986 zero-volume observations and restrict their later analytical use.
- [ ] Finalize exact replacement-index source access and external data redistribution/licensing review. *Non-blocking for the notebook; required before publishing restricted source material or making exact-benchmark claims.*

#### Outstanding External-Data Limitations

- Not every historical ETF price or distribution has been independently verified against an authoritative external source.
- Seven older split events currently rely on secondary-reference records rather than original issuer documents.
- Exact replacement-index availability and relevant redistribution rights require further review.

These limitations are documented in Notebook 01 and carried forward into future stages. They do not prevent completion of the internal data-quality assessment.


#### VIX validation and the revised collection workflow

- [x] Collect FRED VIXCLS from March 2010 to October 30, 2026: 4,350 rows, 122 missing observations.
- [x] Align VIX to the shared ETF calendar: 4,187 valid matches and zero missing dates.
- [x] Investigate the 33 additional VIX observation dates absent from the SOXX calendar.
- [x] Cross-check all 4,187 common ETF VIX closes with Cboe's published series; maximum difference 0.00.
- [x] Screen VIX extremes and numerical integrity; preserve crisis observations and source limitations.
- [x] Preserve existing raw FRED/Cboe VIX snapshots in Notebook 01 rather than overwriting them on reruns.
- [x] Update `check_data.py` to recognize five primary datasets and preserve existing snapshots.
- [x] Verify the **existing-file** collection path: five manifest checksum matches, zero reported errors, and one Cboe reference file.
- [x] Test the revised five-source collection script from an **isolated, empty temporary raw-data directory**, without touching validated source files; record the result.

#### Phase closeout and publication

- [x] Complete the five-source final data-quality assessment (Section 11), including restrictions and remaining limitations.
- [x] Define *intended* date-alignment/adjusted-return/volume/exposure rules without modifying original source data.
- [x] Run the original **four-source** notebook from a fresh kernel successfully, before VIX was added.
- [x] Run the **revised five-source** notebook from a fresh kernel and confirm every cell completes with no errors.
- [x] Review `requirements.txt` and confirm it lists pandas, yfinance, requests, JupyterLab, ipykernel, and Matplotlib. *The notebook has also passed in the existing environment; a clean environment reinstall has not been independently tested.*
- [ ] Finalize any separate `data_sources.md` (if retained in scope); review licensing references, source redistribution boundaries, and README accuracy. *Source-rights work remains open; raw source data is not being published.*
- [ ] Commit the final notebook, collection script, README, requirements and development log; push and verify GitHub status.

**Phase status:** **Five-source analytical validation and reproducibility checks passed; publication pending.** All five primary series have been evaluated, Section 11 is complete, the isolated fresh-download test passed, and the five-source notebook ran from a clean kernel. `requirements.txt` was reviewed against the notebook's reported dependencies. Remaining tasks: complete the final source-rights review, inspect Git changes, commit, push, and verify the remote. Exact benchmark/index-access and provider licensing questions remain documented limitations, not claimed resolved.

### November 9, 2026 — Initial audit and FRED trading calendar

**Objective:** Inspect file size, date validity, duplicates, missing values, and observed nonpositive prices.

| Source | Rows | Missing values | Duplicate dates | Invalid dates | Date range |
|---|---:|---:|---:|---:|---|
| SOXL | 4,187 | 0 | 0 | 0 | 2010-03-11 to 2026-10-30 |
| SOXS | 4,187 | 0 | 0 | 0 | 2010-03-11 to 2026-10-30 |
| SOXX | 4,195 | 0 | 0 | 0 | 2010-03-01 to 2026-10-30 |
| FRED `NASDAQSOX` | 4,350 | 155 | 0 | 0 | 2010-03-01 to 2026-10-30 |

**Investigation:** The initial Terminal audit found no nonpositive observed OHLC/adjusted-close prices in the ETF datasets and no nonpositive *observed* FRED index values. FRED had **155 blank index observations**. Examples include **April 2, 2010** and **May 31, 2010**, dates associated with market closures.

Comparing sets of valid FRED observation dates with SOXX trading dates yielded:

- Valid FRED dates: **4,195**.
- SOXX trading dates: **4,195**.
- Dates in one set but not the other: **0** in each direction.

**Decision:** Keep `nasdaqsox_fred_original.csv` unchanged. When constructing the analysis-ready dataset, exclude FRED rows with missing index values rather than filling them with zeros or forward-filling them without justification.

**What I learned:** An absent value may reflect a closed exchange rather than a missing trading-day price. Date-by-date matching is stronger evidence than merely observing equal row counts.

**Reproducibility status (at this checkpoint):** Missing/duplicate/invalid-date checks and the FRED calendar comparison had been reproduced in Notebook 01. The nonpositive-price test was still pending its Jupyter cell **at that time**; it was completed later (see additional Phase 1.2 entries below).

### November 9, 2026 — ETF trading-date alignment

**Objective:** Ensure cross-ETF comparisons will match observations by date rather than row position.

**Verified findings:** SOXL and SOXS have identical dates. All three ETFs share **4,187** trading dates from **March 11, 2010** through **October 30, 2026**. SOXX has **eight** additional observations before the first SOXL/SOXS date.

**Decision:** Use a date-keyed inner join for three-ETF comparisons. Preserve the early SOXX observations in the source dataset; do not fabricate corresponding SOXL or SOXS prices. The first return that can be calculated inside the shared dataset begins after the first common price observation.

**Reproducibility status:** Completed in Jupyter with a displayed alignment table and the first/last common dates.

### November 9, 2026 — Stock split identification and return consistency

**Objective:** Determine whether split events would create artificial price movements in risk calculations.

**Recorded corporate actions:**

- SOXL: **2 forward splits** — May 20, 2015 (4-for-1) and March 2, 2021 (15-for-1).
- SOXS: **10 reverse splits** — February 24, 2011 (1-for-5); August 20, 2013 (1-for-4); May 20, 2015 (1-for-4); May 1, 2017 (1-for-5); June 28, 2019 (1-for-10); August 28, 2020 (1-for-12); March 28, 2022 (1-for-10); April 15, 2024 (1-for-10); March 5, 2026 (1-for-20); July 15, 2026 (1-for-10).
- SOXX: **1 forward split** — March 7, 2024 (3-for-1).

**Test:** Calculated daily percentage changes in `Close` and `Adj Close` on all **13** recorded split dates. Examples: SOXL **+0.52%** on May 20, 2015; SOXL **−9.42%** on March 2, 2021; SOXS **+3.86%** on March 5, 2026; SOXX **+3.43%** on March 7, 2024. `Close` and `Adj Close` returns matched to two decimal places on those dates, without split-sized discontinuities.

**Interpretation:** The price history appears already split-adjusted. Matching returns on recorded split dates is an **internal consistency check**, not a guarantee that all corporate actions and historical prices are correct.

**Decision:** Do not split-adjust these downloaded `Close`/`Adj Close` histories again. The 13-record reference audit was later completed (see subsequent entry); limits of primary-source verification remain.

**Reproducibility status:** Split dates, readable ratios, and split-day returns have all been reproduced in Jupyter.

### November 9, 2026 — Dividend counts and adjustment context

**Objective:** Separate price-only movements from returns reflecting cash distributions.

| ETF | Recorded dividend events | Historical rows where `Close` differs from `Adj Close` |
|---|---:|---:|
| SOXL | 32 | 4,158 |
| SOXS | 26 | 4,158 |
| SOXX | 65 | 4,161 |

**Example:** On September 23, 2025, SOXS's `Close` return was approximately **−0.379%**, while its `Adj Close` return was approximately **+0.689%**. These are different measures because historical adjusted prices account for distributions.

**What I learned:** A dividend is a distribution to fund shareholders. `Close` and `Adj Close` can differ for thousands of historic rows even though there are far fewer dividend dates, because later distributions affect earlier adjustment factors.

**Provisional methodology:** Use `Adj Close` for historical ETF return and risk calculations, subject to the remaining verification. Retain `Close`, `Dividends`, and `Stock Splits` for independent checks. Do **not** add dividends again to a return already derived from `Adj Close`.

### November 9, 2026 — Investigating exceptionally large SOXS distributions

**Observed anomaly:** SOXS recorded a maximum historical distribution of **684,480,000 USD** on December 14, 2010. Its preceding reported closing price was **15,580,800,000 USD**. Other large reported distributions included **143,040,000 USD** on March 22, 2011 and **12,720 USD** on March 24, 2020.

**Initial diagnostic:** The dividends represented approximately **4.3931%**, **1.1650%**, and **0.1815%**, respectively, of the previous day's correspondingly adjusted closing price. These proportions were far less anomalous than the raw dollar amounts.

**Hypothesis:** Subsequent SOXS reverse splits caused Yahoo's historic dividends and prices to be shown on a later split-adjusted share basis.

**Test:** Identified all later recorded reverse splits for each selected distribution date, multiplied their inverse ratios into a cumulative adjustment factor, and divided the reported dividend and prior close by that factor.

| Historical date | Later reverse-split factor | Reconstructed dividend per historical share | Reconstructed previous close |
|---|---:|---:|---:|
| 2010-12-14 | 960,000,000 | 0.7130 USD | 16.23 USD |
| 2011-03-22 | 192,000,000 | 0.7450 USD | 63.95 USD |
| 2020-03-24 | 240,000 | 0.0530 USD | 29.20 USD |

**Result:** The reconstructed values are consistent with historic per-share distributions expressed before the subsequent reverse splits. This explains how an enormous adjusted historical amount can coexist with an ordinary historical per-share distribution.

**Limitation:** The calculation is based on the splits recorded in the same downloaded dataset. It does not independently certify those splits or dividend amounts. External fund records still need comparison.

**Reproducibility status:** The split-factor calculation and table have been reproduced in Notebook 01. A table was chosen over a chart because it conveys this calculation more precisely.

### November 9, 2026 — Comparing dividend-inclusive and adjusted returns

**Objective:** Test whether daily returns from `Adj Close` agree with a simple formula that adds the distribution to the day's split-adjusted closing price.

The simple cash-dividend-inclusive calculation was:

`100 × ((Close[t] + Dividends[t]) / Close[t−1] − 1)`

This was compared against:

`100 × (AdjClose[t] / AdjClose[t−1] − 1)`

| ETF | Events checked | Mean absolute difference (percentage points) | Maximum absolute difference (percentage points) |
|---|---:|---:|---:|
| SOXL | 32 | 0.01177 | 0.12778 |
| SOXS | 26 | 0.04619 | 0.27464 |
| SOXX | 65 | 0.00313 | 0.01234 |

**Largest example:** SOXS on June 23, 2026 showed approximately **+23.5758%** with the simple dividend-inclusive formula versus **+23.8504%** from `Adj Close`, a difference of **−0.2746 percentage points**.

**Interpretation:** This comparison did *not* prove the dataset was wrong. Adding a cash distribution to the current close is not mathematically identical to Yahoo's backwards dividend-adjustment-factor convention.

### November 9, 2026 — Reconstructing Yahoo's dividend adjustment

**Objective:** Check the adjusted-price calculation against the adjustment convention instead of treating the simple cash-dividend formula as an exact benchmark.

**Method:** On dividend dates without a recorded split, compared `Adj Close` returns against the formula implied by a dividend adjustment factor `1 − Dividends[t] / Close[t−1]`:

`100 × (Close[t] / (Close[t−1] − Dividends[t]) − 1)`

| ETF | Dividend events checked | Mean absolute discrepancy (pp) | Maximum absolute discrepancy (pp) |
|---|---:|---:|---:|
| SOXL | 32 | 0.000009 | 0.000030 |
| SOXS | 26 | 0.000010 | 0.000026 |
| SOXX | 65 | 0.000016 | 0.000067 |

**Result:** The formula reproduced the `Adj Close` daily returns extremely closely. The largest remaining difference across the three funds was approximately **0.000067 percentage points**, on a SOXX distribution date. These residual differences are consistent with limited precision and rounding.

**Methodology decision:** Use `Adj Close` as the **provisional primary ETF return series** for the project. Do not double-count dividends. This finding verifies **internal adjustment consistency**, not the authenticity of the underlying market prices or the completeness of external corporate-action records.

**Reproducibility status:** Both dividend-return comparisons and the Yahoo-formula check have run successfully in Jupyter. The expanded local notebook is not yet confirmed pushed to GitHub.

### November 9, 2026 — Initial extreme daily-return screening in Terminal (later migrated)

**Objective:** Find unusually large ETF moves that might reflect real market volatility or inaccurate data.

**Method:** Calculated daily returns from `Adj Close`, ranked observations by absolute magnitude, and counted days with moves exceeding **30%** in either direction. This was a **screening threshold**, not an automatic error rule.

| ETF | Largest observed daily gain | Largest observed daily loss | Days with absolute return >30% |
|---|---:|---:|---:|
| SOXL | +54.79% | −38.59% | 7 |
| SOXS | +46.25% | −55.98% | 8 |
| SOXX | +18.57% | −15.23% | 0 |

**Notable date:** On **April 9, 2025**, the downloaded series show SOXL **+54.79%**, SOXS **−55.98%**, and SOXX **+18.57%**. The opposite directions and relative magnitudes are broadly plausible for a daily leveraged bull/bear pair versus an unleveraged semiconductor ETF. Plausibility alone is not independent confirmation.

**Other dates identified:** The screening surfaced major moves in **March–April 2020**, **November 10, 2022**, and **June 5, 2026**. These should be corroborated using additional market/source evidence before being marked fully validated.

**Status at this checkpoint:** Terminal screening completed; notebook reproduction and diagnostic visualization were **pending at that time**. See the later Notebook 01 findings entry for their completion.

### November 9, 2026 — Adopting JupyterLab as the analysis workspace

**Objective:** Replace disconnected one-off Terminal analysis snippets with a coherent, reproducible notebook.

**Work completed:**

- Installed **JupyterLab 4.6.6** and **ipykernel 7.4.0** in the project virtual environment, and added notebook dependencies to `requirements.txt`.
- Started JupyterLab from the SOXL project directory and created the `notebooks/` folder and `01_data_validation.ipynb`.
- Added explanatory Markdown, dataset-loading cells, validation output tables, and preliminary findings.
- Saved and pushed the first notebook with commit **`0e2c805`**, alongside the requirements and development log.
- Reproduced missing-data, trading-calendar, ETF-alignment, split-history, and split-return results in Jupyter. Subsequently expanded the local notebook with the SOXS dividend and return-adjustment investigations.

**Issues and fixes:**

1. Initially created a **folder** named `01_data_validation.ipynb` instead of a notebook. Renamed that folder to `notebooks/`, then created the actual `.ipynb` file inside it.
2. Initially had a duplicated `.ipynb` extension in the filename. Renamed the file correctly.
3. The initial dataset-loading cell used `Path.cwd().parent`. Because Jupyter's working directory was already the project root, the code looked for CSVs under `~/Downloads/data/raw/` and raised `FileNotFoundError`. Changing to **`Path.cwd()`** resolved the issue and the expected row counts appeared.
4. Markdown dollar signs in the dividend findings were interpreted as math syntax and damaged the formatting. Replaced that section with headings and a plain Markdown table, then verified that it rendered correctly.

**What I learned:** A Jupyter notebook stores code, outputs, explanations, and results together. The working directory affects file paths; a notebook's location in the sidebar does not necessarily determine its execution directory. Markdown needs careful handling when currency symbols resemble math delimiters.

**Workflow decision:** All exploratory analysis, validation, computations, tables, and helpful visualizations will be performed in Jupyter. Terminal is retained for supporting environment/Git tasks. Standalone `.py` scripts remain appropriate for reusable ingestion and pipeline work. Each notebook has one purpose, and we complete and document it before starting the next.

### November 9, 2026 — Earlier documentation checkpoint (superseded by later work)

**Notebook content at this earlier checkpoint:** Data loading, missing values, FRED calendar checks, ETF alignment, split history/returns, dividend counts, historical SOXS dividend scaling, cash-dividend-return comparison, and Yahoo-adjustment consistency test. **Later work expanded this notebook substantially; see entries below.**

**Validation decision at this earlier checkpoint:** The observed internal checks supported using `Adj Close` as the preliminary ETF return field. Nonpositive-price and extreme-return work, benchmark review, and an initial fresh-kernel run were subsequently completed. Open remaining limitations are described in the latest Phase 1.2 checklist and assessment.

**GitHub status:** Commit `0e2c805` is confirmed published. The expanded local notebook and revised development log require a subsequent verified commit and push. Do not claim they are online until that happens.


### November 9, 2026 — Completing ETF price, return, and corporate-action validation

**Objective:** Extend the initial audit into a reproducible, decision-ready dataset validation notebook.

**Work completed and verified in Jupyter:**

- Confirmed no nonpositive observed ETF OHLC/adjusted-close prices and no nonpositive observed NASDAQSOX index levels. All three ETF datasets passed the OHLC high/low consistency tests and had no negative or missing volume values.
- Screened `Adj Close` returns for unusually large movements. SOXL: largest gain **+54.79%**, largest loss **−38.59%**, **7** days with absolute returns above 30%. SOXS: **+46.25%**, **−55.98%**, **8** days. SOXX: **+18.57%**, **−15.23%**, **0** days.
- Plotted six of the largest semiconductor-sector dates using three ETF return series. Major SOXL/SOXX moves tended to share direction; inverse SOXS tended to move oppositely. FRED NASDAQSOX moves broadly corroborated the market-stress interpretation; neither this pattern nor a sector proxy independently certifies every price.
- Cross-referenced all **13** recorded ETF split dates and ratios: **13 matches**, including **six** designated issuer/primary-reference matches and **seven** designated historical secondary-reference matches. No missing/unlisted events or ratio discrepancies appeared against that reference table.
- Documented the historical benchmark regimes. In the **March–October 2010** overlap, predecessor IGW/SOXX tracked a different index from the leveraged ETFs. From **October 15, 2010** through **June 20, 2021**, their historical index definitions aligned on PHLX; SOXX changed to ICE on **June 21, 2021**, and SOXL/SOXS changed on **August 25, 2021**. Later ICE/NYSE nomenclature changes were recorded. NASDAQSOX is a sector proxy, not the exact leveraged-fund benchmark, from August 25, 2021 onward.
- Examined the October 15, 2010 IGW-to-SOXX identifier transition: no obvious split-sized price discontinuity in the historical adjusted close. Earlier source history must be labelled as predecessor IGW, rather than treated as if the SOXX ticker existed throughout.

**Methods and decisions:** Retain the `Adj Close` return series, avoid double-adjusting for splits or dividends, preserve extreme market observations unless specific errors are demonstrated, and align ETFs by calendar date. Explain historical benchmark regimes when presenting correlations or tracking comparisons.

**Limitations:** The split-reference check tests agreement with collected external reference records, not independent inspection of all issuer action documents. The ETF price series is not independently verified observation-by-observation. Proxy cross-checks demonstrate plausibility, not exact index tracking.

**Visualization decision:** Retain the grouped cross-ETF extreme-date bar chart because it tests whether suspicious returns follow coherent sector and inverse-leverage patterns; use tables for purely numerical validation.

### November 9, 2026 — Investigating historical SOXS volume and the split-adjustment hypothesis

**Objective:** Determine whether trading volume contains hidden quality problems even though OHLC fields are internally consistent.

**Surprise:** SOXS contains **1,986 zero-volume records of 4,187** (**approximately 47.4%**); SOXL and SOXX have no zero-volume records. Of the 1,986 SOXS zero-volume days, **1,976** have a nonzero day-to-day change in reported `Close`.

**Annual investigation:** SOXS had 100% zero-volume records from 2010 through 2016, approximately **96.81%** in 2017, **10.76%** in 2018, and **none from 2019 onward**. The last observed zero was on **August 8, 2018**. An annual bar chart makes the abrupt historical pattern clear.

**Reverse-split analysis:** Calculated the cumulative inverse factors of *subsequent* splits for each observation. Selected median factors were **960,000,000** (2010), **12,000,000** (2015), **2,400,000** (2017–2018), **240,000** (2019), and **10** (2026). Historical split-adjusted share volume could become very small following numerous reverse splits; integer rounding is a plausible contributor to the zeros.

**Troubleshooting:** A NumPy timedelta deprecation warning arose when building a date window around the last zero-volume record. The code was changed from `pd.Timedelta(days=10)` to `pd.DateOffset(days=10)`; it reran without the warning and with unchanged results.

**Methodology decision:** Do **not** interpret early zero-volume records as proof of no actual trading; do not back-calculate lost volume from zero. Preserve raw observations and exclude affected early SOXS volume as a reliable modelling feature unless external records verify it. Do **not** infer invalid ETF prices merely from suspect volume values.

**Unresolved explanation:** The date pattern is consistent with reverse-split adjustment/rounding, but the precise Yahoo-provider procedure and each underlying original volume figure remain unverified.

### November 9, 2026 — Data provenance, raw snapshots and initial four-source completion

**Objective:** Make it possible to distinguish a stable, validated input snapshot from a later provider revision.

- Recorded historical row counts, first/last dates, missing values, and SHA-256 file fingerprints for the original four CSVs. SOXL **4,187**, SOXS **4,187**, SOXX **4,195** and NASDAQSOX **4,350** (including **155** non-observation rows).
- A SHA-256 checksum is a reproducible **file identity fingerprint**; matching one means the bytes are unchanged, **not** that the prices are accurate.
- The raw CSV files remain under `data/raw/` and are ignored by Git. Later feature engineering and database ingestion must use separate processed records rather than alter the originals.
- Wrote the first 10-section version of the notebook's validation assessment. Restarted the kernel and ran the then-current **four-source notebook** successfully from top to bottom.
- Added Matplotlib to the project virtual environment for diagnostic plots. An initial install attempt failed because Terminal was within `notebooks/` and the virtualenv command path was relative to the project root. Moving to the project root resolved the install. **At this earlier checkpoint, the final `requirements.txt` specification still needed review; that review was subsequently completed during the five-source reproducibility checkpoint.**

**Status:** Four-source notebook execution passed at this checkpoint. Subsequent VIX integration means this success is **not** the final five-source fresh-kernel verification.

### November 9, 2026 — Adding the fifth primary dataset: VIXCLS

**Reason for change:** The original project overview called for market-volatility data. To test whether broad S&P 500 options-implied volatility adds information beyond semiconductor/ETF realized volatility, the project added **VIXCLS** as a **candidate** explanatory variable. No predictive benefit has yet been demonstrated.

**Source and coverage:** Downloaded FRED `VIXCLS` from March 1, 2010 through October 30, 2026, yielding **4,350** dated observations including **122** missing values. There were **zero** duplicate or invalid dates and **zero** nonpositive observed VIX values. VIX's published levels measure annualized, approximately 30-day *S&P 500* implied volatility, not semiconductor-specific price volatility or a directional SOXL forecast.

**Alignment:** There are **4,228** valid FRED VIX dates. All **4,195** SOXX trading dates and all **4,187** common SOXL/SOXS/SOXX trading dates have valid VIX closes. The additional **33** valid VIX observations absent from SOXX's trading calendar all fall on U.S. stock-market closure dates, beginning on **May 30, 2022**. These include regularly scheduled market holidays and the special NYSE closure on **January 9, 2025**, for the national day of mourning following former President Jimmy Carter's death. These observations are preserved in the original VIX dataset but excluded from daily ETF-aligned analysis.

**Cross-provider source check:** Retrieved the Cboe historical VIX close CSV separately. On **4,187 of 4,187** common ETF dates, there were **zero** missing Cboe observations and a maximum absolute FRED–Cboe closing difference of **0.00**. The 33 additional FRED records also appeared with matching values in Cboe's published reference file. FRED republishes Cboe information: agreement verifies cross-provider consistency but is **not independent proof of Cboe's underlying index calculation**.

**Extreme-level screening:** Aligned VIX minimum **9.14**, median **16.65**, mean **18.37**, 95th percentile **31.19**, 99th percentile **41.18**, maximum **82.69** (March 16, 2020). Largest absolute daily movement **24.86 index points** (March 16, 2020). The ten highest closes fall in March 2020. Other notable moves include February 2018, August 2011 and April 2025; preserve such plausible stress events rather than clipping them as outliers.

**Decision:** Use FRED `VIXCLS` as the primary historical VIX series, retain Cboe as a separate reference, align to ETF trading dates, and compare risk models with vs without VIX in later walk-forward evaluation. Do not infer predictive power in Notebook 01. Avoid look-ahead leakage: only use a same-day close for a prediction made **after** that value could have been observed.

### November 9, 2026 — Revising five-source acquisition and protecting file snapshots

**Objective:** Make collection reproducible without rewriting source files that have already been audited.

**Problem found:** The original `check_data.py` and early Notebook 01 VIX download cells would overwrite local CSV files each time they ran, potentially changing checksum-identified validation inputs if the providers revised historical data.

**Changes:**

- Extended `check_data.py` from four to **five primary datasets**: SOXL, SOXS, SOXX, FRED NASDAQSOX, and FRED VIXCLS. Retained the explicit FRED date window and `(10, 20)` connection/read timeouts.
- Revised the script to **reuse an existing CSV** rather than silently overwrite it; missing sources are downloaded. Removed the deprecated `raise_errors` argument from the Yahoo retrieval call. Cboe VIX history is a **separate verification reference**, not a sixth primary modelling dataset.
- Changed the notebook's Section 10.2 and Section 10.4 to load preserved FRED and Cboe VIX snapshots where available. Removed a redundant Cboe-file write from Section 10.6.
- The first Jupyter `runpy.run_path(...)` check printed an unnecessarily huge dictionary of Python globals because the final expression returned that mapping. Adding a trailing semicolon suppressed the accidental display; it was an **output-format issue**, not an execution failure.
- Validated five-source inventory and source manifest: SOXL **4,187**, SOXS **4,187**, SOXX **4,195**, NASDAQSOX **4,350** (155 missing), VIXCLS **4,350** (122 missing). All **5 / 5** primary source checksums matched `data/manifest.json`; the original four checksums were unchanged; the Cboe reference file was present; **zero** collection errors were reported.

**Test boundary at this checkpoint:** The revised `check_data.py` existing-file reuse path had passed. The fresh-download test was still outstanding **at this point in the work**; it was subsequently completed successfully in an isolated temporary directory (see final verification entry below). The source-preservation policy protects validated inputs from silent mutation.

### November 9, 2026 — Final five-source assessment drafted; publication still pending

**Notebook deliverable:** Section **11 — Final Data Quality Assessment** is written and rendered. Its scope covers five primary datasets, one Cboe reference file, adjusted-return conventions, source/corporate-action limitations, conditional treatment of SOXS historical volume, VIX validation and use-after-close constraints, and historical index regime distinctions.

**Research plan retained:** Development window **2010–2019**; expanding-window walk-forward tests **2020–2025**; untouched predictive-model holdout **January–October 30, 2026**. Data-quality review of 2026 observations must not be used to select, tune or compare predictive models on the holdout. Evaluate the incremental utility of VIX out of sample; do not assume it improves SOXL downside-risk estimates.

**Overall current assessment:** The available inputs are **conditionally suitable for downstream risk analysis** when using documented date alignment, adjusted-return handling, benchmark regimes and exclusions for unreliable SOXS early volume. This is not a claim that every market price or dividend has been independently confirmed.

**Closeout tasks as originally recorded at this checkpoint (current outcomes below):**

1. **Completed later:** Isolated clean-directory download of all five primary sources; preserved original source CSVs.
2. **Reviewed later:** `requirements.txt` includes pandas, yfinance, requests, JupyterLab, ipykernel, and Matplotlib; notebook executed in the working environment.
3. **Completed later:** Restarted the kernel and ran the revised five-source notebook successfully, including both charts and Section 11.
4. **Still open:** Final cross-check of `README.md` and this log; clarify whether a separate `data_sources.md` is needed, and retain explicit rights/licensing limitations.
5. **Still open:** Inspect Git status/diff, commit the notebook, `check_data.py`, requirements, README, and this development log; push and verify GitHub publication. **No final Stage 1.2 push is confirmed.**

### November 9, 2026 — Final five-source reproducibility and documentation checkpoint

**Objective:** Confirm that the finished data-collection code works both with existing source files and in an empty environment, that the complete validation notebook runs sequentially from a clean kernel, and that the project documentation accurately reflects verified work.

**Isolated fresh-download test:** Executed a copy of `check_data.py` in a disposable temporary directory using the project's active Python interpreter. It fetched **SOXL (4,187 records), SOXS (4,187), SOXX (4,195), NASDAQSOX (4,350), and VIXCLS (4,350)**. The temporary manifest contained **5 / 5** primary sources and **0** errors; exit code was **0**. All five downloaded CSV files existed and were marked `new_download`. SHA-256 checks taken before and after the test confirmed the **original validated snapshots remained unchanged**. The temporary test intentionally contained **0 Cboe reference files**: Cboe is used as an additional historical VIX verification reference, not a sixth primary modelling series.

**Notebook test:** Restarted the Jupyter kernel and successfully ran **every cell of the revised five-source `notebooks/01_data_validation.ipynb`**. Validation tables, both diagnostic charts, VIX/Cboe comparisons, source-inventory checks, the isolated ingestion test, and the final Section 11 assessment executed successfully. This supersedes the earlier four-source test and removes the pending fresh-kernel status.

**Dependency audit:** Reviewed `requirements.txt` entries: `pandas>=2.1,<3`, `yfinance>=0.2.66,<2`, `requests>=2.31,<3`, `jupyterlab>=4.6,<5`, `ipykernel>=7,<8`, and `matplotlib>=3.10,<4`. These cover the stated primary notebook and ingestion imports in the working environment. A clean virtual-environment install from requirements has not been separately tested; do not claim exact cross-platform package reproducibility from broad version ranges.

**Final research decisions:** Keep the validated raw input snapshots, use date-keyed ETF alignment and `Adj Close` returns for preliminary risk analysis, identify benchmark regime changes, restrict unreliable early SOXS volume, and treat VIX as a candidate predictor whose incremental utility remains to be tested out of sample. The entire dataset is **conditionally suitable**, subject to the limitations in Section 11.

**Documentation:** The Stage 1.2 milestone for isolated fresh downloads and clean-kernel execution is marked `[x]` in this log. Confirm the matching checklist item is also checked in `README.md` during the final side-by-side documentation review. The source-licensing/README audit and confirmed GitHub publication milestone remain unchecked. A separate `data_sources.md` is still a planned or optional deliverable, not a completed file.

**GitHub status:** Final Stage 1.2 notebook, script, and documentation changes **not yet confirmed pushed**. Confirm the real Git state and remote push before changing this status or claiming the milestone has been published.

---

## Phase 2 — Exploratory Analysis

### Objective and scope

Explore return dynamics, historical volatility, leverage and sector context without fitting the final predictive model.

**Planned deliverable:** `notebooks/02_exploratory_analysis.ipynb`.

### Stage milestones — mirrored in README

- [ ] Build date-aligned ETF return and volatility comparisons in Notebook 02.
- [ ] Explore drawdowns, leverage effects, semiconductor conditions, and VIX relationships.
- [ ] Document useful visuals and observations without tuning on the 2026 holdout.
- [ ] Validate, document, commit, and publish Notebook 02.

These milestone checkboxes are intentionally identical to the README. The more detailed task list below records the evidence and smaller steps.

### Detailed work checklist (expand during this phase)

- [ ] Inspect adjusted-price returns after applying the 4,187-date inner join; note 1-day return loss from the first aligned observation.
- [ ] Compare SOXL, SOXS and SOXX return distributions, compounding, volatility clustering, drawdown length and sector-market events.
- [ ] Explore VIX levels and changes alongside sector realized volatility without implying forecasting power from descriptive charts.
- [ ] Choose only relevant plots and add interpretation, caveats, and links to Notebook 01 validation decisions.
- [ ] Restart and Run All; update README + log; verify commit and push before next notebook.

**Phase status:** Not started. No work in this phase has been claimed completed.

### Dated work notes

Add entries here as the phase begins. Record evidence, issues, fixes, interpretation, remaining limitations, and verified commit/push status.

---

## Phase 3 — PostgreSQL and SQL

### Objective and scope

Store and transform market data reproducibly in PostgreSQL, with SQL outputs cross-checked against Python.

**Planned deliverable:** `SQL schema, import scripts, and example queries`.

### Stage milestones — mirrored in README

- [ ] Design PostgreSQL tables for sources, trading dates, returns, and metadata.
- [ ] Create reproducible data imports and date-safe SQL transformations.
- [ ] Compare SQL calculations with independently checked Python outputs.
- [ ] Document schema, queries, tests, and the completed SQL milestone.

These milestone checkboxes are intentionally identical to the README. The more detailed task list below records the evidence and smaller steps.

### Detailed work checklist (expand during this phase)

- [ ] Define primary keys, source identifiers, data types, trading-date logic, raw vs normalized layers and corporate-action metadata.
- [ ] Implement rerunnable ingestion; keep raw CSVs out of Git and avoid silently rewriting snapshots.
- [ ] Create SQL views/queries for calendar-aligned returns, volatility summaries and quality flags.
- [ ] Compare selected SQL calculations with notebook/Python reference figures; investigate discrepancies.
- [ ] Include setup instructions, representative safe SQL queries, tests and an independently verified commit.

**Phase status:** Not started. No work in this phase has been claimed completed.

### Dated work notes

Add entries here as the phase begins. Record evidence, issues, fixes, interpretation, remaining limitations, and verified commit/push status.

---

## Phase 4 — Risk Metrics and Feature Engineering

### Objective and scope

Define event labels, risk metrics, and strictly historical predictor features for the agreed 1- and 5-day horizons.

**Planned deliverable:** `notebooks/03_risk_metrics.ipynb`.

### Stage milestones — mirrored in README

- [ ] Define 1-day and 5-day downside outcomes and 10-day/20-day supporting summaries.
- [ ] Calculate downside frequencies, drawdowns, VaR, and other descriptive risk measures in Notebook 03.
- [ ] Build past-only return, realized-volatility, regime, and VIX features.
- [ ] Test data leakage and document the reproducible feature set.

These milestone checkboxes are intentionally identical to the README. The more detailed task list below records the evidence and smaller steps.

### Detailed work checklist (expand during this phase)

- [ ] Confirm exactly how a loss event is defined (e.g., forward 5-day return at or below -10%, if retained as the headline example).
- [ ] Define 1-day/5-day labels and 10-day/20-day supporting risk summaries using future prices only as target outcomes.
- [ ] Calculate drawdowns, empirical downside frequency, historical VaR and suitable risk summaries; specify conventions.
- [ ] Engineer trailing returns, realized volatility, VIX level/change and regime metadata using only past/present information.
- [ ] Check feature timestamps, lags, warm-up gaps, missing values and non-overlap assumptions; rerun and document Notebook 03.

**Phase status:** Not started. No work in this phase has been claimed completed.

### Dated work notes

Add entries here as the phase begins. Record evidence, issues, fixes, interpretation, remaining limitations, and verified commit/push status.

---

## Phase 5 — Volatility Modelling

### Objective and scope

Compare probabilistic downside-risk baselines and test whether regimes and VIX add useful information.

**Planned deliverable:** `notebooks/04_volatility_modeling.ipynb`.

### Stage milestones — mirrored in README

- [ ] Fit unconditional, simple statistical, and volatility-regime risk baselines in Notebook 04.
- [ ] Evaluate whether adding VIX improves risk estimates beyond semiconductor features.
- [ ] Fit preprocessing and regime boundaries using training data only.
- [ ] Document assumptions, comparisons, and a versioned modelling milestone.

These milestone checkboxes are intentionally identical to the README. The more detailed task list below records the evidence and smaller steps.

### Detailed work checklist (expand during this phase)

- [ ] Define the unconditional benchmark and at least one continuous-volatility/statistical baseline.
- [ ] Fit simple logistic or comparable probabilistic models plus clearly defined volatility-regime methods.
- [ ] Determine thresholds, feature transformations and model parameters only inside training windows.
- [ ] Conduct a controlled comparison of candidate models with and without VIX; avoid inferring value from in-sample correlation.
- [ ] Document leakage controls, model rationale, versioned code and reproducible outputs.

**Phase status:** Not started. No work in this phase has been claimed completed.

### Dated work notes

Add entries here as the phase begins. Record evidence, issues, fixes, interpretation, remaining limitations, and verified commit/push status.

---

## Phase 6 — Walk-Forward Evaluation

### Objective and scope

Measure genuinely out-of-sample prediction quality with time-ordered evaluation in 2020–2025.

**Planned deliverable:** `notebooks/05_backtesting.ipynb`.

### Stage milestones — mirrored in README

- [ ] Run expanding-window out-of-sample evaluation across 2020–2025 in Notebook 05.
- [ ] Assess calibration, Brier scores, VaR/Kupiec tests, and uncertainty.
- [ ] Account for overlapping forecast horizons and record negative results.
- [ ] Freeze the final modelling decisions before opening the 2026 holdout.

These milestone checkboxes are intentionally identical to the README. The more detailed task list below records the evidence and smaller steps.

### Detailed work checklist (expand during this phase)

- [ ] Specify the expanding training-window schedule and the 2020–2025 evaluation windows before fitting.
- [ ] Produce out-of-sample probabilities and diagnostics by date/horizon; compare with baselines fairly.
- [ ] Compute calibration, Brier scores, relevant VaR exceedance diagnostics and Kupiec tests with assumptions documented.
- [ ] Estimate uncertainty, account for overlapping 5-day outcomes, and preserve poor/negative findings.
- [ ] Lock the selection rule, model configuration and evaluation plan before opening the 2026 holdout.

**Phase status:** Not started. No work in this phase has been claimed completed.

### Dated work notes

Add entries here as the phase begins. Record evidence, issues, fixes, interpretation, remaining limitations, and verified commit/push status.

---

## Phase 7 — 2026 Holdout and Case Study

### Objective and scope

Evaluate pre-locked models on 2026 and explain a semiconductor selloff in terms of leverage and volatility.

**Planned deliverable:** `Frozen holdout results and case-study analysis`.

### Stage milestones — mirrored in README

- [ ] Evaluate the frozen approach once on the January–October 2026 holdout.
- [ ] Investigate a 2026 semiconductor selloff and leverage/compounding effects.
- [ ] Present holdout performance, uncertainty, benchmark caveats, and limitations.
- [ ] Commit a reproducible holdout and case-study milestone.

These milestone checkboxes are intentionally identical to the README. The more detailed task list below records the evidence and smaller steps.

### Detailed work checklist (expand during this phase)

- [ ] Run the locked evaluation on January–October 30, 2026 without changing methods in response to holdout outcomes.
- [ ] Distinguish data-quality use of 2026 from model-fitting/model-selection use of 2026.
- [ ] Quantify a selected 2026 selloff with SOXL/SOXS/SOXX paths, leveraged compounding, volatility and VIX context.
- [ ] Explain interpretation limits: benchmark changes, non-causal relationships, data revisions and model uncertainty.
- [ ] Archive results and verify a reproducible case-study commit before reporting the final conclusion.

**Phase status:** Not started. No work in this phase has been claimed completed.

### Dated work notes

Add entries here as the phase begins. Record evidence, issues, fixes, interpretation, remaining limitations, and verified commit/push status.

---

## Phase 8 — Power BI and Final Portfolio Release

### Objective and scope

Communicate verified findings through two Power BI pages, reproducible assets, and an honest GitHub project narrative.

**Planned deliverable:** `Power BI report (exactly two pages), final summary and portfolio release`.

### Stage milestones — mirrored in README

- [ ] Build exactly two Power BI pages for risk monitoring and model evaluation.
- [ ] Write the executive summary, key findings, and responsible interpretation.
- [ ] Publish reproducibility instructions, representative visuals, and portfolio walkthrough.
- [ ] Complete appropriate automated checks and verify the final GitHub release.

These milestone checkboxes are intentionally identical to the README. The more detailed task list below records the evidence and smaller steps.

### Detailed work checklist (expand during this phase)

- [ ] Design Page 1 for risk context and market regimes; Page 2 for validation, backtest results and holdout interpretation.
- [ ] Build clear slicers/filters and consistent metric definitions; test them against source/SQL/Python outputs.
- [ ] Prepare an executive summary emphasizing findings, limitations, and uncertainty rather than trading claims.
- [ ] Publish safe example screenshots/demo assets without redistributing unlicensed market data.
- [ ] Add appropriate smoke tests/CI, environment setup, versioned assets and a verifiable final GitHub release.

**Phase status:** Not started. No work in this phase has been claimed completed.

### Dated work notes

Add entries here as the phase begins. Record evidence, issues, fixes, interpretation, remaining limitations, and verified commit/push status.

---

## Template for future phase entries

### Phase X.X — Phase title

**Objective and scope:** Explain the question, deliverable, and why the phase matters.

**Stage milestones — mirrored in README:** Copy the stage’s concise milestone checklist exactly from `README.md`, keeping checked states synchronized.

**Detailed work checklist:** Break those milestones into smaller verifiable steps before starting the stage.

**Dated work:** Record each meaningful session *under its stage*, including results, errors, fixes, interpretations, limitations, and the confirmed GitHub status.

### YYYY-MM-DD — Work session or milestone

**Objective:**\
**Work completed:**\
**Issue or surprise:**\
**Investigation / attempted fixes:**\
**Results and verification:**\
**Decision and what I learned:**\
**Open limitations:**\
**Next steps:**\
**GitHub status:** Not committed / committed locally / pushed and verified.
