import sqlite3
import pandas as pd

DB_PATH = "db/nifty100.db"

conn = sqlite3.connect(DB_PATH)

companies = pd.read_sql("SELECT * FROM companies", conn)
ratios = pd.read_sql("SELECT * FROM financial_ratios", conn)

# Merge on company_id
merged = pd.merge(
    companies,
    ratios,
    left_on="id",
    right_on="company_id",
    how="inner"
)

log = []

for _, row in merged.iterrows():

    # ROE check
    if (
        pd.notna(row.get("roe_percentage"))
        and pd.notna(row.get("return_on_equity_pct"))
    ):
        diff = abs(
            row["roe_percentage"] -
            row["return_on_equity_pct"]
        )

        if diff > 5:
            log.append(
                f"{row['company_name']} | ROE difference = {diff:.2f}%"
            )

with open("output/ratio_edge_cases.log", "w") as f:

    for line in log:
        f.write(line + "\n")

print(f"{len(log)} edge cases written.")
