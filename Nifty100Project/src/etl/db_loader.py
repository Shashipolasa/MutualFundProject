import sqlite3
import pandas as pd
from pathlib import Path
HEADERS = {
    "companies.xlsx": 1,
    "analysis.xlsx": 1,
    "balancesheet.xlsx": 1,
    "prosandcons.xlsx": 1,
    "cashflow.xlsx": 1,
    "documents.xlsx": 1,
    "financial_ratios.xlsx": 0,
    "market_cap.xlsx": 2,
    "stock_prices.xlsx": 2,
    "peer_groups.xlsx": 1,
    "sectors.xlsx": 1,
    "profitandloss.xlsx": 1
}
DB_PATH = "db/nifty100.db"
RAW_PATH = Path("data/raw")

FILES = {
    "companies.xlsx": "companies",
    "analysis.xlsx": "analysis",
    "balancesheet.xlsx": "balancesheet",
    "cashflow.xlsx": "cashflow",
    "documents.xlsx": "documents",
    "financial_ratios.xlsx": "financial_ratios",
    "peer_groups.xlsx": "peer_groups",
    "profitandloss.xlsx": "profitandloss",
    "prosandcons.xlsx": "prosandcons",
    "sectors.xlsx": "sectors",
    "stock_prices.xlsx": "stock_prices",
    "market_cap.xlsx": "market_cap"
}

conn = sqlite3.connect(DB_PATH)

for file_name, table_name in FILES.items():
    file_path = RAW_PATH / file_name

    print(f"Loading {file_name} -> {table_name}")

    df = pd.read_excel(file_path, header=HEADERS[file_name])


    # NOTE:
    # We will adjust header/column names after checking each file.
    df.to_sql(table_name, conn, if_exists="replace", index=False)

print("All files loaded successfully.")

conn.close()
