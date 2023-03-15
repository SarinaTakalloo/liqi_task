#first try to connect to google colab in order to have access to google sheets
from google.colab import auth
import pandas as pd
import gspread
from google.auth import default

auth.authenticate_user()
creds, _ = default()
gc = gspread.authorize(creds)
auth.authenticate_user()

worksheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1TAkUt6RygXEMIFp59L5GS15l-YWDjupOH1WI9XM6M0k/edit#gid=0').sheet1
rows = worksheet.get_all_values()




# reading data
def read_data(WS):
  rows = WS.get_all_values()
  df = pd.DataFrame.from_records(rows[1:] , columns = ['date', 'categories', 'amount'])
  return df


def preprocess_data(df):
  df['amount'] = df['amount'].str.replace('€', '').str.replace(' ', '').str.replace(',', '').astype(float)
  df['in_flow'] = df[df['amount'] > 0]['amount']
  df['out_flow'] = df[df['amount'] < 0]['amount']
  return df

def calculate_parameters(df):
  TR = df_transaction.loc[df_transaction['categories'].isin(['INCASSO FATTURA','EROGAZIONE FINANZIAMENTO']), 'amount'].sum()
  EX = df_transaction.loc[df_transaction['categories'].isin(['STIPENDI', 'UTENZE' , 'PAGAMENTO FORNITORI','PAGAMENTO FATTURA']), 'amount'].sum()
  DT = df_transaction.loc[df_transaction['categories'].isin(['RIMBORSO FINANZIAMENTO']), 'amount'].sum()
  return TR,EX,DT

def calculate_ratios(df):
  debt_to_liability_ratio = abs(debt/operating_expenses)
  debt_service_coverage_ratio = (total_revenue - abs(operating_expenses))/abs(debt)
  current_ratio = total_revenue/abs(debt + operating_expenses)
  return debt_to_liability_ratio, debt_service_coverage_ratio, current_ratio


def calculate_max_amount(df):
  debt_to_liability_ratio, debt_service_coverage_ratio, current_ratio = calculate_ratios(df)
  if ((debt_to_liability_ratio < 0.1) and (debt_service_coverage_ratio > 1) and (current_ratio > 1)):
    maximum_amount_to_be_granted = cash_balance
    print(maximum_amount_to_be_granted)
  else:
    raise ValueError("Company's health is not approved")



try:
  df_transaction = preprocess_data(read_data(worksheet))
  total_revenue, operating_expenses, debt = calculate_parameters(df_transaction)
  cash_balance = total_revenue - abs(operating_expenses + debt)
  max_amount = calculate_max_amount(df_transaction)
    print("Maximum amount that can be granted: ", max_amount)
except Exception as e:
    print("An error occurred: ", str(e))


##in this task there is no need to calculate the average monthly cash flow. 
##however, to have a better insight of what's going on every month, I made this part available 
#calculate in-flow and out-flow and group by month to monitor every month cash balance
#df['data'] = pd.to_datetime(df['data'])
#df['month'] = df['data'].dt.month

#df['in-flow'] = df[df['amount'] > 0]['amount']
#df['out-flow'] = df[df['amount'] < 0]['amount']
#monthly = df.groupby('month').agg({'in-flow': "sum", 'out-flow': "sum"})

## Calculate average monthly inflow and outflow
#avg_inflow = monthly['in-flow'].mean()
#avg_outflow = monthly['out-flow'].mean()
## Calculate cash balance for each month
#monthly['Cash Balance'] = monthly['in-flow'] + monthly['out-flow']
#max_cash_balance = monthly['Cash Balance'].max()


