# Import this on ratios.py
# This contains functions for calculating financial ratios

def gross_margin_percentage(gross_margin: float or int, sales: float or int):
    return f"{round((gross_margin / sales) * 100, 2)}%"

def net_operating_margin_percentage(EBIT: float or int, sales: float or int):
    return f"{round((EBIT / sales) * 100, 2)}%"

def operating_leverage(contribution: float or int, fixed_costs: float or int):
    return f"{round(contribution / fixed_costs, 2)}"