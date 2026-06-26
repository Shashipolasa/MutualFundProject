from src.analytics.cashflow_kpis import *

def test_fcf():
    assert free_cash_flow(100, -20) == 80

def test_quality():
    assert cfo_quality(200, 100) == "High Quality"

def test_quality2():
    assert cfo_quality(70, 100) == "Moderate"

def test_quality3():
    assert cfo_quality(30, 100) == "Accrual Risk"

def test_capex():
    assert capex_intensity(-50, 1000) == "Moderate"

def test_conversion():
    assert fcf_conversion(80, 100) == 80
