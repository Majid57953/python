import pandas as pd
df=pd.DataFrame({'id':[1,2,3,4,5],'man_id':[2,1,1,1,1]})
print(df.groupby('man_id').count())
ms=df.groupby('man_id').count().reset_index()
ms2=df.groupby('man_id').size()
print(ms)
print(ms2)
managers_with_four_or_more=ms2[ms2>=4]
print(ms[ms['id']>3])
print(managers_with_four_or_more)
#print(df[df['id']].isin(managers_with_four_or_more))