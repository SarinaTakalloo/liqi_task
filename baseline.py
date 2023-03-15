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

print(rows)



# reading data
import pandas as pd
df = pd.DataFrame.from_records(rows[1:] , columns = ['data', 'categories', 'amount'])
print(df.dtypes)

#access to the month of each transaction
df['data'] = pd.to_datetime(df['data'])
df['month'] = df['data'].dt.month


