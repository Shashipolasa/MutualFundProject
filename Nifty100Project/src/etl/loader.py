from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw")

FILES = {
    "companies.xlsx": "companies",
    "analysis.xlsx": "analysis",
    "balancesheet.xlsx": "balancesheet",
    "cashflow.xlsx": "cashflow",
    "documents.xlsx": "documents",
    "financial_ratios.xlsx": "financial_ratios",
    "market_cap.xlsx": "market_cap",
    "peer_groups.xlsx": "peer_groups",
    "profitandloss.xlsx": "profitandloss",
    "prosandcons.xlsx": "prosandcons",
    "sectors.xlsx": "sectors",
    "stock_prices.xlsx": "stock_prices",
}


def load_file(file_name):
    file_path = RAW_PATH / file_name

    df = pd.read_excel(file_path)

    print("=" * 70)
    print(file_name)
    print("Rows :", len(df))
    print("Columns :", len(df.columns))
    print(df.head())

    return df


def main():
    datasets = {}

    for file in FILES:
        datasets[file] = load_file(file)

    print("\nSuccessfully loaded", len(datasets), "datasets.")


if __name__ == "__main__":
    main()
