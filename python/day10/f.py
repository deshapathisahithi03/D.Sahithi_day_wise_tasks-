import pandas as pd
df=pd.read_csv('data.csv')
print(df.sort_values(by='State',ascending=False))