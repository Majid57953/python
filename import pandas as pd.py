import pandas as pd
import numpy as np
my_series=pd.Series(data=[2,3,4,5],index=[3,4,5,6])
print(my_series)
mydict={
    'name':['Majid','John'],
    'age':[33,34],
    'gender':['male','male'],
    'siblings':1
    }
df=pd.DataFrame(mydict)
df['salary']=1000
print(df)
del df['salary']
print(df)
print(df.shape)
print(df.describe())
print(df.loc[0])
my_series=pd.Series(mydict)

print(my_series)
print(mydict)
print(mydict.keys())
mydict.keys()
myl=[8,18,22,18,9]
numpar=np.array(myl)
print(numpar)
print(8 in myl)
print(myl)
myl.remove(18)
print(myl)
df=pd.read_csv('11.csv')
#print(df)
#print(4+5)