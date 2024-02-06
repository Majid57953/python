import pandas as pd
df=pd.DataFrame({"id":[1,1,1],'uid':[4,3,4],'sid':[6,1,4]})
print(df)
df2=df.groupby('id').nunique()

print(df2.rename({'uid':'unique'},inplace=True))

