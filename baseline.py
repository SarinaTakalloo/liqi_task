#first try to connect to google colab in order to have access to google sheets
from google.colab import auth
auth.authenticate_user()

import gspread
from google.auth import default
creds, _ = default()

gc = gspread.authorize(creds)
auth.authenticate_user()

worksheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1TAkUt6RygXEMIFp59L5GS15l-YWDjupOH1WI9XM6M0k/edit#gid=0').sheet1
rows = worksheet.get_all_values()




# reading data
import pandas as pd
df = pd.DataFrame.from_records(rows[1:] , columns = ['data', 'categories', 'amount'])
print(df.dtypes)

#access to the month of each transaction
df['data'] = pd.to_datetime(df['data'])



# Calculate inflow and outflow for each month (this is based of negative and positive amount in the transaction file)
#convert the amount column to float
df['amount'] = df['amount'].str.replace('€', '')
df['amount'] = df['amount'].str.replace(' ','')
df['amount'] = df['amount'].str.replace(',','')
df['amount'] =df['amount'].astype(float)

#calculate in-flow and out-flow and group by month to monitor every month cash balance
df['in-flow'] = df[df['amount'] > 0]['amount']
df['out-flow'] = df[df['amount'] < 0]['amount']


##in this task there is no need to calculate the average monthly cash flow. 
##however, to have a better insight of what's going on every month, I made this part available 
#df['month'] = df['data'].dt.month
#monthly = df.groupby('month').agg({'in-flow': "sum", 'out-flow': "sum"})


## Calculate average monthly inflow and outflow
#avg_inflow = monthly['in-flow'].mean()
#avg_outflow = monthly['out-flow'].mean()
## Calculate cash balance for each month
#monthly['Cash Balance'] = monthly['in-flow'] + monthly['out-flow']
#max_cash_balance = monthly['Cash Balance'].max()





#calculate all the positive amount and negative amount as current assets and liabilities/debts respectively and the obtaining current available cash
in_flow , out_flow = df.agg({'in-flow': "sum", 'out-flow': "sum"})
current_cash = in_flow - abs(out_flow)

#I have considered the current assets as INCASSO FATTURA and EROGAZIONE FINANZIAMENTO; but, in reality to determine correct current assets, 
#other type of data is needed such as cash, cash equivalents, short-term investments, accounts receivable, inventory, supplies, and prepaid expenses.
#in this task there are only funding distributions and invoice collection

total_revenue = df.loc[df['categories'].isin(['INCASSO FATTURA','EROGAZIONE FINANZIAMENTO']), 'amount'].sum()
operating_expenses = df.loc[df['categories'].isin(['STIPENDI', 'UTENZE' , 'PAGAMENTO FORNITORI','PAGAMENTO FATTURA']), 'amount'].sum()
debt = df.loc[df['categories'].isin(['RIMBORSO FINANZIAMENTO']), 'amount'].sum()

#calculate different ratios:

debt_to_liability_ratio = debt/operating_expenses
debt_service_coverage_ratio = (total_revenue - operating_expenses)/debt
current_ratio = total_revenue/(debt + operating_expenses)





