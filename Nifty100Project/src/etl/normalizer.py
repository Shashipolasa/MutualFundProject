def normalize_year(year):
    """Convert year to integer."""
    try:
        return int(str(year).strip())
    except:
        return None


def normalize_ticker(ticker):
    """Standardize company ticker."""
    if ticker is None:
        return None
    return str(ticker).strip().upper()
