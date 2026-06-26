import sqlite3
import pandas as pd

from ratios import (
    net_profit_margin,
    operating_profit_margin,
    roe,
    debt_to_equity,
    interest_coverage,
    asset_turnover,
)

DB_PATH = "db/nifty100.db"

conn = sqlite3.connect(DB_PATH)

profitandloss = pd.read_sql("SELECT * FROM profitandloss", conn)
balancesheet = pd.read_sql("SELECT * FROM balancesheet", conn)

df = pd.merge(
    profitandloss,
    balancesheet,
    on=["company_id", "year"],
    how="inner"
)

results = []

for _, row in df.iterrows():

    result = {
        "company_id": row["company_id"],
        "year": row["year"],

        "net_profit_margin_pct": net_profit_margin(
            row["net_profit"],
            row["sales"]
        ),

        "operating_profit_margin_pct": operating_profit_margin(
            row["operating_profit"],
            row["sales"]
        ),

        "return_on_equity_pct": roe(
            row["net_profit"],
            row["equity_capital"],
            row["reserves"]
        ),

        "debt_to_equity": debt_to_equity(
            row["borrowings"],
            row["equity_capital"],
            row["reserves"]
        ),

        "interest_coverage": interest_coverage(
            row["operating_profit"],
            row["other_income"],
            row["interest"]
        ),

        "asset_turnover": asset_turnover(
            row["sales"],
            row["total_assets"]
        )
    }

    results.append(result)

ratio_df = pd.DataFrame(results)

ratio_df.to_sql(
    "financial_ratios",
    conn,
    if_exists="replace",
    index=False
)

print("=" * 50)
print("Financial Ratio Engine Completed")
print(f"Rows Generated : {len(ratio_df)}")
print("=" * 50)

conn.close()
