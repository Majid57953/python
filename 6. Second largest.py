import pandas as pd
employee=pd.DataFrame({
    "Id":[1,2,3,4],
    "salary":[100,200,300,400]
})

def returnSec(employee:pd.DataFrame):
    max_val=employee['salary'].max()
    #sec_query=employee.query('salary!=@max_val')
    sec_query=employee[employee['salary']!=max_val]
    #sec_query=employee.filter(employee['salary']!=max_val)
    print(sec_query)
    sec_val=sec_query['salary'].max()
    return sec_val
#     series=employee['Salary'].nlargest(2)
#     max_val=employee['Salary'].max()
#     print(series[2])
#     print(series[1])
#     print(max_val)
#     try:
#         if (series[1]!=series[0]) | (series[1]!=max_val):
#             return pd.DataFrame({'SecondHighestSalary':[series[1]]})
#         else:
#             return pd.DataFrame({'SecondHighestSalary':[None]})   
#     except:
#         return pd.DataFrame({'SecondHighestSalary':[None]})   
print(returnSec(employee))