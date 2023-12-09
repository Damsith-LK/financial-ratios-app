# Import this on main.py
# Contains information about different financial ratios

import functions

ratios_dict = {
    "gross-margin-percentage":
        {
            "name": "Gross Margin Percentage",
            "description": "Gross margin is sales minus cost of goods sold. If the gross isn't there, there will be no net income."
                           " How high gross margin percentage needs to be depends on how a business is organized and the costs"
                           " it has to support. The higher the gross margin percentage, the better.",
            "labels": ["Gross margin", "Sales"],
            "function": functions.gross_margin_percentage
         },
    "net-operating-margin-percentage":
        {
            "name": "Net Operating Margin Percentage",
            "description": "Net Operating Margin Percentage tells you the net profitability of the operations of the business "
                           "before you factor in your taxes and cost of money. EBIT stands for Earnings Before Interest "
                           "and Taxes, or sales minus all costs of being in that business, not including capital costs."
                           " Businesses with high net operating margin percentages are typically stronger than those with low percentages.",
            "labels": ["EBIT", "Sales"],
            "function": functions.net_operating_margin_percentage
        },
    "operating-leverage":
        {
            "name": "Operating leverage",
            "description": "Operating leverage is the percentage of fixed costs in a company's cost structure. It can be calculated "
                           "by dividing contribution by fixed costs. Contribution refers to the gross margin(sales - cost of goods sold) minus"
                           " variable costs(all costs that are not fixed costs that fluctuate with sales). Fixed costs include all sales, "
                           "general and administrative costs that are fixed and do not fluctuate based on sales volume. "
                           "Fixed costs are sometimes referred as overhead. A business that has an operating leverage "
                           "of 1 is generating just enough revenue to pay for its fixed costs. This would mean that there "
                           "is no return for the owners. The higher the operating leverage, the better.",
            "labels": ["Contributions", "Fixed costs"],
            "function": functions.operating_leverage
        }
}