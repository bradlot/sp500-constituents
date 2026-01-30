# S&P 500 Ticker Fetcher

A lightweight Python script to fetch the current list of S&P 500 constituent tickers.

## What It Does
- Scrapes the official table from [Wikipedia's List of S&P 500 companies](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
- Extracts only the ticker symbols (e.g., `AAPL`, `MSFT`).
- Saves them to a plain text file `sp500.csv` (one ticker per line, no header).

## How to Run

1. **Set up environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run the script**:
   ```bash
   python get.py
   ```

3. **Output**:
   The script creates (or overwrites) `sp500.csv` in the current directory.

## Attribution
Data sourced from [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies) under the [CC BY-SA 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/).

## Disclaimer
This is an unofficial list generated from public data. Always verify with official sources for critical financial use.
