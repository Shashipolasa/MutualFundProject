def free_cash_flow(operating_activity, investing_activity):
    return operating_activity + investing_activity


def cfo_quality(cfo, pat):
    if pat == 0:
        return None

    ratio = cfo / pat

    if ratio > 1:
        return "High Quality"
    elif ratio >= 0.5:
        return "Moderate"
    else:
        return "Accrual Risk"


def capex_intensity(investing_activity, sales):
    if sales == 0:
        return None

    ratio = abs(investing_activity) / sales * 100

    if ratio < 3:
        return "Asset Light"
    elif ratio <= 8:
        return "Moderate"
    else:
        return "Capital Intensive"


def fcf_conversion(fcf, operating_profit):
    if operating_profit == 0:
        return None
    return (fcf / operating_profit) * 100
