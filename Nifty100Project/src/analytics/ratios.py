def net_profit_margin(net_profit, sales):
    if sales == 0:
        return None
    return (net_profit / sales) * 100


def operating_profit_margin(operating_profit, sales):
    if sales == 0:
        return None
    return (operating_profit / sales) * 100


def roe(net_profit, equity_capital, reserves):
    total_equity = equity_capital + reserves
    if total_equity <= 0:
        return None
    return (net_profit / total_equity) * 100


def roce(ebit, equity_capital, reserves, borrowings):
    capital = equity_capital + reserves + borrowings
    if capital <= 0:
        return None
    return (ebit / capital) * 100


def roa(net_profit, total_assets):
    if total_assets == 0:
        return None
    return (net_profit / total_assets) * 100

def debt_to_equity(borrowings, equity_capital, reserves):
    total_equity = equity_capital + reserves
    if borrowings == 0:
        return 0
    if total_equity <= 0:
        return None
    return borrowings / total_equity


def interest_coverage(operating_profit, other_income, interest):
    if interest == 0:
        return None
    return (operating_profit + other_income) / interest


def net_debt(borrowings, investments):
    return borrowings - investments


def asset_turnover(sales, total_assets):
    if total_assets == 0:
        return None
    return sales / total_assets
