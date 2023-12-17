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

def debt_to_equity_ratio(total_liabilities: float or int, total_equity: float or int):
    return f"{round(total_liabilities / total_equity, 2)}"

def quick_ratio(liquid_assets: float or int, current_liabilities: float or int):
    return f"{round(liquid_assets / current_liabilities, 2)}"

def current_ratio(current_assets: float or int, current_liabilities: float or int):
    return f"{round(current_assets / current_liabilities, 2)}"

def pe_ratio(market_price: float or int, net_income: float or int):
    return f"{round(market_price / net_income, 2)}"

def return_on_equity(net_income: float or int, shareholder_equity: float or int):
    return f"{round(net_income / shareholder_equity)}"

def cash_on_cash_return(positive_net_cash_return: float or int, down_payment: float or int):
    return f"{round((positive_net_cash_return / down_payment) * 100, 1)}%"