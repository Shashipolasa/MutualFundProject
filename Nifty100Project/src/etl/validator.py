import pandas as pd


def check_null_primary_key(df, column_name):
    """DQ-01: Primary key should not contain NULL values."""
    return df[df[column_name].isnull()]


def check_duplicate_primary_key(df, column_name):
    """DQ-02: Primary key should be unique."""
    return df[df.duplicated(subset=[column_name], keep=False)]


def check_duplicate_company_year(df):
    """DQ-03: (company_id, year) must be unique."""
    return df[df.duplicated(subset=["company_id", "year"], keep=False)]
