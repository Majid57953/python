import pandas as pd
list=[1,5,3,7,2]
list.sort()
print(list)
df=pd.DataFrame({'id':[2,1],'email':['mmaa@kk','mmaa@kk']})
df.sort_values(by='id',ascending=True,inplace=True)
print(df)
df.drop_duplicates(subset='email',inplace=True)
print (df)