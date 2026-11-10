"""Day 1: confirm available SOXL/SOXS/SOXX and PHLX SOX daily data.

This is a source availability check, not a validated trading/backtest dataset.
The project's fixed data cutoff is October 30, 2026 inclusive.
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
END_EXCLUSIVE = "2026-10-31"  # Includes Friday, October 30, 2026.
TICKERS = ("SOXL", "SOXS", "SOXX")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def report(label: str, df: pd.DataFrame, date_col: str) -> None:
    dates = pd.to_datetime(df[date_col], errors="coerce")
    print(f"  {label}: {len(df):,} records | {dates.min().date()} to {dates.max().date()}")
    print(f"    Duplicate dates: {dates.duplicated().sum()} | Bad dates: {dates.isna().sum()}")


def fetch_etf(ticker: str) -> dict:
    print(f"\nFetching {ticker} from Yahoo Finance using yfinance...")
    df = yf.Ticker(ticker).history(
        start=START,
        end=END_EXCLUSIVE,
        interval="1d",
        auto_adjust=False,  # Preserve Close and dividend/split-adjusted Adj Close.
        actions=True,       # Include Dividends and Stock Splits when returned.
        raise_errors=True,
        timeout=30,
    )
    if df.empty:
        raise RuntimeError("Provider returned no daily observations")
    df = df.rename_axis("Date").reset_index()
    df["Date"] = pd.to_datetime(df["Date"], utc=True).dt.strftime("%Y-%m-%d")
    path = RAW / f"{ticker.lower()}_yahoo_daily.csv"
    df.to_csv(path, index=False)
    report(ticker, df, "Date")
    print(f"    Columns: {', '.join(df.columns)}")
    if "Adj Close" not in df.columns:
        print("    WARNING: Missing Adj Close; investigate before any return calculations.")
    if "Stock Splits" in df.columns:
        print(f"    Split events returned: {(pd.to_numeric(df['Stock Splits'], errors='coerce').fillna(0) != 0).sum()}")
    print(f"    Saved: {path.relative_to(ROOT)}")
    return {
        "file": str(path.relative_to(ROOT)),
        "sha256": sha256(path),
        "rows": len(df),
        "first_date": df["Date"].iloc[0],
        "last_date": df["Date"].iloc[-1],
        "columns": list(df.columns),
        "source": "Yahoo Finance via yfinance; adjusted values may be revised retroactively",
    }


def fetch_fred_sox() -> dict:
    print("\nFetching pre-2021 benchmark series NASDAQSOX from FRED...")
    url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=NASDAQSOX"
    response = requests.get(url, timeout=40, headers={"User-Agent": "Mozilla/5.0 SOXL-risk-education-project"})
    response.raise_for_status()
    path = RAW / "nasdaqsox_fred_original.csv"
    path.write_bytes(response.content)
    df = pd.read_csv(io.BytesIO(response.content))
    date_col = next((col for col in ("observation_date", "DATE", "date") if col in df.columns), None)
    if date_col is None:
        raise RuntimeError(f"Unexpected FRED file columns: {list(df.columns)}")
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    window = df[(df[date_col] >= pd.Timestamp(START)) & (df[date_col] < pd.Timestamp(END_EXCLUSIVE))].copy()
    report("FRED NASDAQSOX (filtered period)", window, date_col)
    print("    IMPORTANT: Nasdaq SOX is the historical fund benchmark only before Aug 25, 2021.")
    print("    After that date, it is a proxy, NOT the exact ICE/NYSE benchmark.")
    print(f"    Saved source snapshot: {path.relative_to(ROOT)}")
    return {
        "file": str(path.relative_to(ROOT)),
        "sha256": sha256(path),
        "window_rows": len(window),
        "source": "FRED series NASDAQSOX; Nasdaq PHLX Semiconductor price index",
        "source_url": url,
    }


def main() -> None:
    manifest = {
        "captured_utc": datetime.now(timezone.utc).isoformat(),
        "data_start": START,
        "fixed_cutoff_inclusive": "2026-10-30",
        "data_end_exclusive": END_EXCLUSIVE,
        "sources": {},
        "errors": {},
    }
    for ticker in TICKERS:
        try:
            manifest["sources"][ticker] = fetch_etf(ticker)
        except Exception as exc:
            manifest["errors"][ticker] = str(exc)
            print(f"  ERROR retrieving {ticker}: {exc}")
    try:
        manifest["sources"]["FRED_NASDAQSOX"] = fetch_fred_sox()
    except Exception as exc:
        manifest["errors"]["FRED_NASDAQSOX"] = str(exc)
        print(f"  ERROR retrieving NASDAQSOX: {exc}")
    path = ROOT / "data" / "manifest.json"
    path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"\nManifest: {path.relative_to(ROOT)}")
    print(f"Sources downloaded: {len(manifest['sources'])} | Issues: {len(manifest['errors'])}")
    if manifest["errors"]:
        print("Share the errors with ChatGPT; don't substitute data silently.")
    print("\nNEXT: check source coverage and ICE/NYSE benchmark licensing before modelling.")


if __name__ == "__main__":
    main()
