import pandas as pd

employee=pd.DataFrame({
    "Id":[1,2,3,4,5],
    "Salary":[100,200,300,300,500]
})

def get_largest(employee:pd.DataFrame,n):
    salaries=employee['Salary'].nlargest(n)
    min_salary=salaries.min()
    max_salary=salaries.max()
    employee_max=employee.query('Salary==@min_salary')  
    print (employee_max['Id'].max())
    if len(salaries) ==n and employee_max['Id'].count()==1:
        return pd.DataFrame({'getNthHighestSalary({})'.format(n):[salaries.iloc[-1]]})
    else:
        return pd.DataFrame({'getNthHighestSalary({})'.format(n):[None]})
    

print(get_largest(employee,2))

