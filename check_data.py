"""Collect original SOXL/SOXS/SOXX, NASDAQSOX, and VIXCLS daily sources.

This is an availability/provenance check, not a validated backtest dataset.
Fixed historical cutoff: October 30, 2026 (inclusive).

Safety rule: existing raw source snapshots are NEVER overwritten. When a CSV
already exists, the script reuses it and records its current SHA-256 checksum.
"""

from __future__ import annotations

import hashlib
import io
import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests
import yfinance as yf

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "data" / "raw"
RAW.mkdir(parents=True, exist_ok=True)

START = "2010-03-01"
END_INCLUSIVE = "2026-10-30"
END_EXCLUSIVE = "2026-10-31"  # Yahoo's history end parameter is exclusive.
TICKERS = ("SOXL", "SOXS", "SOXX")

FRED_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv"
CBOE_REFERENCE_URL = (
    "https://cdn-api.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def report(label: str, df: pd.DataFrame, date_col: str) -> None:
    dates = pd.to_datetime(df[date_col], errors="coerce")
    if dates.notna().sum() == 0:
        raise ValueError(f"{label}: no valid dates found")
    print(
        f"  {label}: {len(df):,} records | "
        f"{dates.min().date()} to {dates.max().date()}"
    )
    print(
        f"    Duplicate dates: {dates.duplicated().sum()} | "
        f"Bad dates: {dates.isna().sum()}"
    )


def fetch_etf(ticker: str) -> dict:
    path = RAW / f"{ticker.lower()}_yahoo_daily.csv"

    if path.exists():
        print(f"\nReusing existing {ticker} Yahoo Finance snapshot (not overwritten)...")
        df = pd.read_csv(path)
        file_status = "reused_existing"
    else:
        print(f"\nFetching {ticker} from Yahoo Finance using yfinance...")
        df = yf.Ticker(ticker).history(
            start=START,
            end=END_EXCLUSIVE,
            interval="1d",
            auto_adjust=False,  # Keep both Close and adjusted Adj Close.
            actions=True,       # Keep Dividends and Stock Splits.
            timeout=30,
        )
        if df.empty:
            raise RuntimeError("Provider returned no daily observations")

        df = df.rename_axis("Date").reset_index()
        df["Date"] = (
            pd.to_datetime(df["Date"], utc=True).dt.strftime("%Y-%m-%d")
        )
        # The file is written only if it does not already exist.
        df.to_csv(path, index=False)
        file_status = "new_download"

    if df.empty or "Date" not in df.columns:
        raise ValueError(f"{ticker}: empty file or missing Date column")

    report(ticker, df, "Date")
    dates = pd.to_datetime(df["Date"], errors="coerce")
    if dates.isna().any() or dates.duplicated().any():
        raise ValueError(f"{ticker}: invalid or duplicate dates; investigate source")

    print(f"    Columns: {', '.join(df.columns)}")
    if "Adj Close" not in df.columns:
        print("    WARNING: Missing Adj Close; investigate before return calculations.")
    if "Stock Splits" in df.columns:
        split_count = (
            pd.to_numeric(df["Stock Splits"], errors="coerce")
            .fillna(0).ne(0).sum()
        )
        print(f"    Split events returned: {split_count}")
    print(f"    File: {path.relative_to(ROOT)}")

    return {
        "file": str(path.relative_to(ROOT)),
        "file_status": file_status,
        "sha256": sha256(path),
        "rows": len(df),
        "first_date": dates.min().strftime("%Y-%m-%d"),
        "last_date": dates.max().strftime("%Y-%m-%d"),
        "columns": list(df.columns),
        "source": "Yahoo Finance via yfinance; historical adjustments may be revised",
    }


def fetch_fred_series(series_id: str, filename: str) -> dict:
    path = RAW / filename
    source_url = (
        f"{FRED_URL}?id={series_id}&cosd={START}&coed={END_INCLUSIVE}"
    )

    if path.exists():
        print(f"\nReusing existing FRED {series_id} snapshot (not overwritten)...")
        raw_bytes = path.read_bytes()
        file_status = "reused_existing"
    else:
        print(f"\nFetching FRED {series_id}...")
        response = requests.get(source_url, timeout=(10, 20))
        response.raise_for_status()
        raw_bytes = response.content
        file_status = "new_download"

    # Parse and verify the returned contents before saving a newly fetched file.
    df = pd.read_csv(io.BytesIO(raw_bytes))
    date_col = next(
        (col for col in ("observation_date", "DATE", "date") if col in df),
        None,
    )
    if date_col is None or series_id not in df.columns:
        raise ValueError(
            f"FRED {series_id}: unexpected columns {list(df.columns)}"
        )

    dates = pd.to_datetime(df[date_col], errors="coerce")
    if dates.isna().any() or dates.duplicated().any():
        raise ValueError(f"FRED {series_id}: invalid or duplicate dates")

    in_window = dates.between(START, END_INCLUSIVE)
    window = df.loc[in_window].copy()
    window[date_col] = dates.loc[in_window]
    if window.empty:
        raise ValueError(f"FRED {series_id}: no observations in requested period")

    values = pd.to_numeric(window[series_id], errors="coerce")
    report(f"FRED {series_id} (filtered period)", window, date_col)
    print(f"    Missing index values: {values.isna().sum()}")

    if not path.exists():
        path.write_bytes(raw_bytes)

    if series_id == "NASDAQSOX":
        print("    NOTE: historical SOXL/SOXS index reference before Aug 25, 2021;")
        print("    sector proxy afterward, not the exact ICE/NYSE benchmark.")
    else:
        print("    NOTE: VIX is S&P 500 implied volatility, not semiconductor-specific.")

    print(f"    File: {path.relative_to(ROOT)}")
    return {
        "file": str(path.relative_to(ROOT)),
        "file_status": file_status,
        "sha256": sha256(path),
        "window_rows": len(window),
        "missing_index_values": int(values.isna().sum()),
        "first_date": window[date_col].min().strftime("%Y-%m-%d"),
        "last_date": window[date_col].max().strftime("%Y-%m-%d"),
        "source": f"FRED {series_id}",
        "source_url": source_url,
    }


def main() -> dict:
    manifest = {
        "manifest_generated_utc": datetime.now(timezone.utc).isoformat(),
        "data_start": START,
        "fixed_cutoff_inclusive": END_INCLUSIVE,
        "data_end_exclusive_for_yahoo": END_EXCLUSIVE,
        "snapshot_policy": "Reuse existing raw CSVs; never overwrite automatically",
        "sources": {},
        "reference_sources": {},
        "errors": {},
    }

    for ticker in TICKERS:
        try:
            manifest["sources"][ticker] = fetch_etf(ticker)
        except Exception as exc:
            manifest["errors"][ticker] = str(exc)
            print(f"  ERROR checking {ticker}: {exc}")

    fred_series = (
        ("FRED_NASDAQSOX", "NASDAQSOX", "nasdaqsox_fred_original.csv"),
        ("FRED_VIXCLS", "VIXCLS", "vix_fred_original.csv"),
    )
    for key, series_id, filename in fred_series:
        try:
            manifest["sources"][key] = fetch_fred_series(series_id, filename)
        except Exception as exc:
            manifest["errors"][key] = str(exc)
            print(f"  ERROR checking {series_id}: {exc}")

    # Reference data supports source verification but is not a sixth model input.
    cboe_path = RAW / "vix_cboe_original.csv"
    if cboe_path.exists():
        manifest["reference_sources"]["CBOE_VIX"] = {
            "file": str(cboe_path.relative_to(ROOT)),
            "sha256": sha256(cboe_path),
            "source_url": CBOE_REFERENCE_URL,
            "purpose": "Official published VIX historical closing-value cross-check",
        }

    manifest_path = ROOT / "data" / "manifest.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"\nManifest: {manifest_path.relative_to(ROOT)}")
    print(
        f"Primary sources present: {len(manifest['sources'])} / 5 | "
        f"Issues: {len(manifest['errors'])}"
    )
    print(f"Cboe reference files: {len(manifest['reference_sources'])}")
    if manifest["errors"]:
        print("Investigate the errors; do not silently substitute data.")
    return manifest


if __name__ == "__main__":
    main()
