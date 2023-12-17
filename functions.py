# Import this on ratios.py
# This contains functions for calculating financial ratios

def gross_margin_percentage(gross_margin: float or int, sales: float or int):
    return f"{round((gross_margin / sales) * 100, 2)}%"

def net_operating_margin_percentage(EBIT: float or int, sales: float or int):
    return f"{round((EBIT / sales) * 100, 2)}%"

def operating_leverage(contribution: float or int, fixed_costs: float or int):
    return f"{round(contribution / fixed_costs, 2)}"

def financial_leverage(total_capital_employed: float or int, shareholder_equity: float or int):
    return f"{round(total_capital_employed / shareholder_equity, 2)}"

def total_leverage(operating_leverage: float or int, financial_leverage: float or int):
    return f"{round(operating_leverage * financial_leverage, 2)}"

def debt_to_equity_ratio(total_liabilites: float or int, total_equity: float or int):
    return f"{round(total_liabilites / total_equity, 2)}"