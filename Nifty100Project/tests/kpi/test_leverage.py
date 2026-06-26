from src.analytics.ratios import *

def test_debt_free():
    assert debt_to_equity(0, 100, 100) == 0

def test_interest_zero():
    assert interest_coverage(100, 20, 0) is None

def test_net_debt():
    assert net_debt(1000, 400) == 600

def test_asset_turnover():
    assert asset_turnover(1000, 500) == 2
