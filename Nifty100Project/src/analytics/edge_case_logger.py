import sqlite3
import pandas as pd
import os

DB_PATH = "db/nifty100.db"

conn = sqlite3.connect(DB_PATH)

companies = pd.read_sql("SELECT * FROM companies", conn)
ratios = pd.read_sql("SELECT * FROM financial_ratios", conn)

# Rename id -> company_id if required
if "id" in companies.columns:
    companies = companies.rename(columns={"id": "company_id"})

os.makedirs("output", exist_ok=True)

merged = companies.merge(ratios, on="company_id", how="inner")

with open("output/ratio_edge_cases.log", "w") as f:

    for _, row in merged.iterrows():

        source_roe = row.get("roe_percentage")
        calc_roe = row.get("return_on_equity_pct")

        if pd.notna(source_roe) and pd.notna(calc_roe):

            diff = abs(source_roe - calc_roe)

            if diff > 5:
                f.write(
                    f"{row['company_id']} | "
                    f"ROE Difference = {diff:.2f}% | "
                    f"Category: Formula discrepancy\n"
                )

print("ratio_edge_cases.log generated successfully.")

conn.close()
