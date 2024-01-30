import pandas as pd
df=pd.DataFrame({'id':[1,2,2,2],'subject':[1,1,2,2]})
print(df)
print(df.groupby('id')['subject'].nunique())