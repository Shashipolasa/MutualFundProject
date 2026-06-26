from src.analytics.ratios import *

def test_net_profit_margin():
    assert net_profit_margin(10, 100) == 10

def test_zero_sales():
    assert net_profit_margin(10, 0) is None

def test_roe():
    assert roe(20, 50, 50) == 20

def test_negative_equity():
    assert roe(20, -50, 20) is None

def test_roa():
    assert roa(20, 100) == 20

def test_zero_assets():
    assert roa(20, 0) is None
