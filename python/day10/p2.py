import pandas as pd
data={
    'Region':['North','South','East'],
    'State':['J&K','TG','AP'],
    'Year':[2023,2024,2021],
    'Sales':[1245300,89067790,1557800],
    'profit':[4567,789965,89765]
        
}
df=pd.DataFrame(data)
df.set_index(['Region','Year'],inplace=True)
print(df)
df.to_csv('data.csv',index=False)
print(df.loc[('South', 2024), 'Sales'])
df_sales=pd.DataFrame({'State':['J&K','TG'],'Sales':[1245300,89067790],})
df_profit=pd.DataFrame({'State':['J&K','TG'],'profit':[4567,789965],})
df_merged=pd.merge(df_sales,df_profit,on='State',how='inner')
df_merged=pd.merge(df_sales,df_profit,on='State',how='left')
print(df_merged)