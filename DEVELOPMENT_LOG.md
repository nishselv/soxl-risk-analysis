# Development Log — SOXL Risk Analysis

*A chronological record of implementation, choices, troubleshooting, and lessons learned for the Version 2.2 project.*

**Main project overview:** [README.md](README.md)  
**Current state:** Initial setup pushed to GitHub; historical data-source verification is next.

---

## How this log is maintained

For each meaningful work session, record:

- **Date and objective:** What I intended to accomplish.
- **Work completed:** The actual commands, scripts, analysis, or outputs produced.
- **Issues and investigation:** What failed, evidence/error messages, what I tried, and what happened.
- **Decisions and reasoning:** Why I chose an approach or rejected an alternative.
- **Verification:** How I checked that the work was correct.
- **Next steps:** What remains open.

An unresolved issue should stay labeled **Open** until the fix is tested. Git commit history is the record of code changes; this journal records the reasoning behind them.

---

## November 2026 — Project initialization

### Objective

Set up a reproducible local development environment and establish a GitHub repository for a Python, PostgreSQL/SQL, and Power BI analysis of leveraged semiconductor ETF downside risk.

### Work completed

1. Established the **Version 2.2** project scope. SOXL is the primary analysis asset; SOXS is used for comparison. The fixed historical cutoff is **October 30, 2026**.
2. Created the local project directory `~/Downloads/Personal Project - SOXL` on macOS.
3. Set up a Python **3.14.7** virtual environment (`.venv`) and installed the initial project dependencies.
4. Created `check_data.py` for initial source-availability checks. The script requests daily SOXL, SOXS, and SOXX histories through `yfinance` and requests FRED series `NASDAQSOX` through `requests`.
5. Added early checks/reporting for duplicate dates, invalid dates, missing adjusted-close information, and split-event counts where returned. The script saves raw CSV files and a JSON manifest with retrieval metadata and SHA-256 checksums.
6. Added `.gitignore` to avoid committing the virtual environment, downloaded market-data snapshots, and temporary files.
7. Created the initial `README.md` and `requirements.txt`.

### Issue 001 — FRED semiconductor-index request timed out

**Status: Resolved November 9, 2026 (see resolution below)**

- **Observed:** Initial downloads for SOXL, SOXS, and SOXX succeeded, but the FRED `NASDAQSOX` request timed out.
- **Relevant implementation:** `check_data.py` uses an HTTP request with a 40-second timeout to retrieve a CSV from `fred.stlouisfed.org`.
- **Why it matters:** A missing benchmark series prevents completion of the intended source-validation stage. In addition, this series is not the fund's exact benchmark after the fund's August 2021 benchmark change.
- **What has *not* been established:** Whether the timeout was transient, network-related, or caused by the endpoint; no successful benchmark download has been confirmed.
- **Planned next diagnostic:** Test the CSV URL independently with `curl`, inspect the returned HTTP status and file content, and then decide whether code changes are needed.
- **Decision:** Keep the error visible in the data manifest. Do not replace the benchmark silently or start modelling with incomplete source validation.

### November 9, 2026 — First Git commit and GitHub push

**Objective:** Publish the project foundation and link the local `main` branch to GitHub.

**Verified work:**

- Initial commit created: `ff4a457` — `Initial setup: SOXL Risk Analysis Project`.
- Four files included: `.gitignore`, `README.md`, `check_data.py`, `requirements.txt`.
- Added `origin` pointing to `https://github.com/nishselv/soxl-risk-analysis.git`.
- Verified the Git remote URL for both fetch and push using `git remote -v`.
- Ran `git push -u origin main` successfully. Terminal reported `main -> main` and established tracking of `origin/main`.

**Result:** The initial repository setup is published. The data-source issue remains open.

### November 9, 2026 — Documentation redesign

**Objective:** Separate the portfolio-facing project overview from the detailed development journal.

**Decision:** Keep `README.md` concise and focused on the research problem, methods, deliverables, status, and eventual findings. Maintain this file as the dated record of work, encountered errors, attempted fixes, verification, and lessons learned. Keep data-source documentation in the planned `data_sources.md` rather than putting every technical detail on the front page.

**Next steps:** Add and commit the redesigned documentation; then return to FRED connectivity and source validation.

---


### November 9, 2026 — FRED download issue resolved

**Objective:** Retrieve all four historical data sources successfully.

**What I learned:** FRED stands for Federal Reserve Economic Data. It is a free database maintained by the Federal Reserve Bank of St. Louis. This project uses FRED's NASDAQSOX series for historical semiconductor-market context. NASDAQSOX is not SOXL's exact benchmark throughout the study period.

**Issue:** The original Python request to FRED repeatedly timed out after 40 seconds, although SOXL, SOXS, and SOXX downloaded correctly.

**Investigation:**
1. Tested FRED using curl with explicit start and end dates. HTTP 200; 79,937 bytes downloaded in approximately 1.31 seconds.
2. Inspected the CSV, confirming dates from March 1, 2010 through October 30, 2026.
3. Tested Python requests independently with the same bounded URL. HTTP 200; 79,937 bytes downloaded.
4. Updated check_data.py to use the date-bounded FRED URL and separate connection/read timeouts.
5. Reran the complete Python script.

**Verified result:** All four data sources downloaded successfully. The FRED series returned 4,350 records, with zero duplicate dates and zero invalid dates. The script reported `Sources downloaded: 4 | Issues: 0`.

**Conclusion:** The updated request resolved the observed failure. The exact reason for the earlier timeouts remains uncertain. Successful downloading does not yet establish that all market data and adjustments are analytically valid.

**Additional issue:** yfinance displays a deprecation warning concerning `raise_errors`. This did not prevent the downloads and will be addressed separately.

**Next steps:** Verify source coverage, adjusted prices, distributions, split handling, benchmark changes and licensing before modelling.

---

## Upcoming work (Version 2.2)

- [ ] Resolve FRED connectivity and verify benchmark coverage/definitions.
- [ ] Complete data validation and document sources, adjustments, date coverage, and limitations in `data_sources.md`.
- [ ] Build PostgreSQL ingestion and analytical SQL transformations.
- [ ] Implement leakage-safe volatility features and statistical risk baselines.
- [ ] Evaluate walk-forward forecasts over 2020–2025; preserve the separate 2026 holdout.
- [ ] Assess calibration, Brier scores, VaR, and uncertainty under overlapping outcomes.
- [ ] Complete the 2026 selloff decomposition.
- [ ] Create exactly two Power BI dashboard pages.
- [ ] Add automated tests, final findings, executive summary, and demonstration assets.

---

## Template for the next entry

```markdown
### YYYY-MM-DD — Short title

**Objective:**

**Work completed:**

**Issue or surprise:**

**Investigation / attempted solutions:**

**Result and verification:**

**Decision / what I learned:**

**Next steps:**
```
