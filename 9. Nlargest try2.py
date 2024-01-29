import pandas as pd

df=pd.DataFrame({'id':[1,2,3],'salary':[100,200,300]})

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    series=employee.nlargest(N,columns='salary')
    max_val=series['salary'].max()
    
    ser2=series.query('salary==@max_val')
    max_id=series['id'].min()
    print(len(series))
    print(max_id)
    if (len(series)>=N) & ((max_id==N)):
        return pd.DataFrame({'getNthHighestSalary({})'.format(N):[series.iloc[-1,1]]})
    else:
        return pd.DataFrame({'getNthHighestSalary({})'.format(N):[None]})
print(nth_highest_salary(df,2))