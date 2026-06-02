import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

files = [
    "02_nav_history_clean.csv",
    "07_scheme_performance_clean.csv",
    "08_investor_transactions_clean.csv"
]

for file in files:
    table_name = file.replace(".csv", "").replace("_clean", "")

    df = pd.read_csv(f"data/processed/{file}")

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"{table_name}: {len(df)} rows loaded")

print("Database created successfully")