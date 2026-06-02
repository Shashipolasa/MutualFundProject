import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Fix dates
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

# Keep only valid types
valid_types = ["Sip", "Lumpsum", "Redemption"]
df = df[df["transaction_type"].isin(valid_types)]

# Amount must be positive
df = df[df["amount_inr"] > 0]

# Validate KYC status
valid_kyc = ["Verified", "Pending", "Rejected"]
invalid_kyc = df[~df["kyc_status"].isin(valid_kyc)]

print("Invalid KYC records:", len(invalid_kyc))

# Remove duplicates
df = df.drop_duplicates()

df.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("Transactions cleaned successfully")