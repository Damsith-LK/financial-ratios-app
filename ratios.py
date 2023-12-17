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
        },
    "quick-ratio": {
        "name": "Quick ratio",
        "description": "In finance, the quick ratio, also known as the acid-test ratio is a type of liquidity ratio, "
                       "which measures the ability of a company to use its near-cash or 'quick' assets to extinguish or "
                       "retire its current liabilities immediately.",
        "labels": ["Liquid assets", "Current liabilities"],
        "function": functions.quick_ratio
        },
    "current-ratio": {
        "name": "Current ratio",
        "description": "The current ratio is a liquidity ratio that measures a company’s ability to pay short-term obligations "
                       "or those due within one year. It tells investors and analysts how a company can maximize the current "
                       "assets on its balance sheet to satisfy its current debt and other payables.",
        "labels": ["Current assets", "Current liabilities"],
        "function": functions.current_ratio
        },
    "pe-ratio": {
        "name": "P/E Ratio",
        "description": "The price-to-earnings ratio is the ratio for valuing a company that measures its current share "
                       "price relative to its earnings per share (EPS). The price-to-earnings ratio is also sometimes "
                       "known as the price multiple or the earnings multiple."
                       "P/E ratios are used by investors and analysts to determine the relative value of a company's "
                       "shares in an apples-to-apples comparison to others in the same sector. It can also be used to "
                       "compare a company against its own historical record or to compare aggregate markets against one "
                       "another or over time.",
        "labels": ["Market price (per share)", "Net income (per share)"],
        "function": functions.pe_ratio
        },
    "return-on-equity": {
        "name": "Return on equity",
        "description": "Return on equity (ROE) is a measure of financial performance calculated by dividing net income "
                       "by shareholders' equity. Because shareholders' equity is equal to a company’s assets minus its "
                       "debt, ROE is considered the return on net assets. ROE is considered a gauge of a corporation's "
                       "profitability and how efficient it is in generating profits. The higher the ROE, the more "
                       "efficient a company's management is at generating income and growth from its equity financing",
        "labels": ["Net income", " Shareholders' equity"],
        "function": functions.return_on_equity
        },
    "cash-on-cash-return": {
        "name": "Cash-on-cash return",
        "description": "A cash-on-cash return is a rate of return often used in real estate transactions that calculates "
                       "the cash income earned on the cash invested in a property. Let's say you bought an apartment "
                       "building for $500,000. You put $100,000 down and secure a mortgage for the $400,000 balance. "
                       "You have a monthly cash flow of $2,000 after all expenses and the mortgage payment. Your cash-on-cash "
                       "return is 24 percent or $24,000 ($2,000 x 12 months) divided by $100,000.",
        "labels": ["Positive net cash flow", "Down payment"],
        "function": functions.cash_on_cash_return
    }
}