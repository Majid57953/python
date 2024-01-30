import pandas as pd
employeedf=pd.DataFrame({'Name':['John','Sara','Calvin','Will'],'salary':[100,200,200,300],
                         'departmentid':[1,1,1,2]})
deparmentdf=pd.DataFrame({'id':[1,2],'Name':['Sales','Corporative']})
def department_highest_salary(employee:pd.DataFrame,department:pd.DataFrame):
    employee['rank']=employee.groupby('departmentid')['salary'].rank(method='dense',ascending=False)
    return employee[employee['rank']==1]

print(department_highest_salary(employeedf,deparmentdf))
