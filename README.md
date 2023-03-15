# liqi_task
In this repository, the solution related to the assigned task is published.

### OBJECTIVE: 
To prepare a report for the lending manager to help him/her decide whether to approve the short-term (<12 months) funding request from ABC Company. To do this you have at your disposal:
* Current account transactions during 2022 (https://docs.google.com/spreadsheets/d/1lqaobayFAdTrGP4l8uFyK8YYm7ixO4IHO--nRjk23zY)
* Any other public data sources you can think of

### REQUIREMENTS:
* The report must specify as its main output the maximum amount that can be granted to the company (along with the rationale for the choice)
* Python language
* Code reachable on your personal github (or preferred git hosting) 

### SOLUTION:

In order to overcome this issue the reader must understand a precise answer needs more information on the data. Therefore, it's difficult to determine whether a company is able to borrow money based solely on the provided categories; however, some information can be extracted such as total revenue(INVOICE COOLECTION and FUNDING DISTRIBUTION, liabilities(UTILITIES, SALARY, and PAYMENTS) and debt(LOAN PAYMENT).
Considering this information three ratio are introduced: ebt-to-liability ratio, debt service coverage ratio and current ratio which each discuss different aspects of financial health of company. These three ratios as there are other factors that lenders may consider when evaluating a company's creditworthiness. We can interpret the ratios based on their numbers.


These ratios are obtained as **0.0514, 1.420** and **1.021** for **debt-to-liability, service coverage** and **current ratio respectively**.


The debt-to-liability ratio: This ratio measures the amount of debt a company has in relation to its total liabilities. It is calculated by dividing the company's total debt by its total liabilities. A high debt-to-liability ratio may indicate that the company has taken on too much debt relative to its overall financial obligations. Conversly, the number 0.0514 indicates that the company has a low amount of debt relative to its total liabilities. This may be viewed positively by lenders as it indicates that the company has a lower risk of defaulting on its debt obligations.

The debt service coverage ratio: This ratio measures a company's ability to meet its debt payments. It is calculated by dividing the company's net operating income (income minus expenses) by its total debt service (the total amount of principal and interest payments due on all of its loans). A higher debt service coverage ratio indicates that a company is better able to meet its debt obligations.Therefore, ratio of 1.420 indicates that the company is generating enough operating income to cover its debt payments. This is generally viewed positively by lenders as it indicates that the company is financially stable and has the ability to repay its debts.

The current ratio: This ratio measures the amount of current assets which in this task are considered as **invoice collection** and **funding distributions** with respect to the current liabilities that, in this task are defined as **loan payment** and **expenses**. Consequently, 1.021 indicates that the company has enough current assets to cover its current liabilities. This is also viewed positively by lenders as it indicates that the company is able to meet its short-term obligations.

Lenders may use the debt service coverage ratio to determine whether a company can generate enough income to repay the debt. Typically, lenders will require a DSCR of at least 1.2 or 1.25, meaning that the company's operating income is at least 1.2 or 1.25 times the amount of its debt payments. Based on the DSCR of 1.420 in this example, it appears that the company's income is sufficient to cover its debt payments.

Lenders may also consider the current ratio as an indicator of a company's ability to repay its debts. A current ratio of 1.0 or higher is generally viewed positively as it indicates that the company has enough current assets to cover its current liabilities. However, lenders may also consider other factors such as the quality and liquidity of the company's assets.

However, lenders typically use a variety of factors when determining how much money to lend, including the company's credit history, cash flow, revenue, collateral, and other financial and non-financial considerations. 

For short-term funding requests (less than 12 months), lenders may consider the company's cash flow projections and ability to generate sufficient cash to repay the loan within the specified timeframe. The lender may also consider the company's creditworthiness, including its credit score, payment history, and other factors that may indicate its ability to repay the loan.

Based on this information, the lender may offer a loan amount that is commensurate with the company's ability to repay the loan within the specified timeframe, while also taking into account any collateral or other factors that may mitigate the risk of default. In this example, this amount is considered equal to the cash flow of the company within a year. Meaning, the money after subtracting expenses and debt from total revenue which is equal to 7525.14 euros. 






