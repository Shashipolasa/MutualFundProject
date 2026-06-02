import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Numeric columns
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Flag expense ratio anomalies
anomalies = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("Expense Ratio Anomalies:", len(anomalies))

# Remove duplicates
df = df.drop_duplicates()

df.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("Performance data cleaned successfully")