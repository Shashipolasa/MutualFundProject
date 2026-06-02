import pandas as pd
import os

DATA_PATH = "data/raw"

files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

print("=" * 50)
print("DATA INGESTION REPORT")
print("=" * 50)

for file in files:
    print(f"\n\nProcessing: {file}")

    df = pd.read_csv(os.path.join(DATA_PATH, file))

    print("Shape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())