import re

def normalize_year(year):
    """
    Convert different year formats to YYYY.
    Examples:
    FY24 -> 2024
    FY2023 -> 2023
    2022 -> 2022
    """

    year = str(year).strip().upper()

    if year.startswith("FY"):
        year = year.replace("FY", "")

    year = re.sub(r"[^0-9]", "", year)

    if len(year) == 2:
        return int("20" + year)

    return int(year)


def normalize_ticker(ticker):
    """
    Normalize stock ticker names.
    """

    ticker = str(ticker).strip().upper()
    ticker = ticker.replace(".NS", "")
    ticker = ticker.replace(" ", "")

    return ticker
