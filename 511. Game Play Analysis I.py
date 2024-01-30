import pandas as pd
df=pd.DataFrame({'id':[1,2,1],'date':[2021,2022,2022]})

print(df.groupby('id')['date'].min().reset_index(name='first'))