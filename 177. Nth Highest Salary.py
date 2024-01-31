import pandas as pd
df=pd.DataFrame({'id':[1,2,3],'salary':[100,200,300]})
df2=pd.DataFrame({'id':[1],'salary':[100]})
df3=pd.DataFrame({'id':[1,2],'salary':[100,100]})
df4=pd.DataFrame({'id':[3,2,1],'salary':[1,0,0]})
print(df4.shape[0])
def highest(N:int,employee:pd.DataFrame):
    employee.drop_duplicates(subset="salary", inplace=True)
    if employee.shape[0] < N or N <= 0:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})

    else:
        return pd.DataFrame(
            {
                f"getNthHighestSalary({N})": 
                [employee["salary"].sort_values(ascending=False).iloc[N-1]]})
    # dfn=employee.nlargest(N,columns='salary')
    # max_val=dfn['salary'].max()
    # cmv=dfn.query('salary==@max_val')['salary'].count()
    # if len(dfn)<N or cmv!=1:
    #     return pd.DataFrame({f'getNthHighestSalary({N})':[None]})
    # else:
    #     return pd.DataFrame({f'getNthHighestSalary({N})':[dfn.iloc[-1,1]]})
    
print(highest(3,df4))