import pandas as pd
df=pd.DataFrame({'Id':[1,2,3],'Value':[200,400,300]})
df2=df.sort_values(by='Value',ascending=False)
df3=df2.reset_index()
df3.rename(columns={'Id':'test'},inplace=True)
print(df3['Value'].loc[0])
print(df3.loc[0])