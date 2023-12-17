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
        },
    "financial-leverage":
        {
            "name": "Financial leverage",
            "description": "Financial leverage refers to the degree to which an investor or a business uses borrowed money. "
                           "Total capital employed is the book or accounting value of all interest-bearing debt(leave out "
                           "payables for goods to be resold and liabilities due to wages, expenses, and taxes owed but not "
                           "yet paid), plus all owners equity. So if you have $50,000 of debt and $50,000 of shareholder's "
                           "equity, your financial leverage would be 2(or $100,000 divided by $50,000).",
            "labels": ["Total capital employed", "Shareholders' equity"],
            "function": functions.financial_leverage
        },
    "total-leverage":
        {
            "name": "Total leverage",
            "description": "Total leverage is the risk that a company carries in its present business. Total leverage tells "
                           "you the total effect a given change in the business should have on the equity owners. If you "
                           "are the business owner, and therefore on the inside, your company's total leverage is at least "
                           "partly under your control. Well-run, conservatively managed (publicly traded) American companies "
                           "usually keep the total-leverage figure under 5.",
            "labels": ["Operating leverage", "Financial leverage"],
            "function": functions.total_leverage
        },
    "debt-to-equity-ratio":
        {
            "name": "Debt-to-equity ratio",
            "description": "Debt-to-equity ratio measures just that, the portion of the whole enterprise (total liabilities) "
                           "financed by outsiders in the proportion to the part financed by insiders (total equity). "
                           "Most businesses try to stay at a ratio of one-to-one or below. Generally speaking, the lower "
                           "the debt-to-equity ratio, the more conservative the financial structure of the company.",
            "labels": ["Total liabilities", "Total equity"],
            "function": functions.debt_to_equity_ratio
        }
}