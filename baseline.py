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


##in this task there is no need to calculate the average monthly cash flow however, to have a better insight of what's going on every month, I made this part available 
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

#I have considered the currents assets as INCASSO FATTURA and EROGAZIONE FINANZIAMENTO; but, in reality to determine a correct assets, 
#other data is needed such as cash, cash equivalents, short-term investments, accounts receivable, inventory, supplies, and prepaid expenses.
#in this task there are only funding distributions and invoice collection
current_assets = df.loc[df['categories'].isin(['INCASSO FATTURA','EROGAZIONE FINANZIAMENTO']), 'amount'].sum()




