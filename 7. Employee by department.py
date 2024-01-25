import pandas as pd
emp_data = [
    ["Alice", 25, "Sales", 1],
    ["Bob", 35, "Marketing", 2],
    ["Charlie", 35, "Marketing", 2],
    ["David", 40, "IT", 4]
]
# create a dataframe from the list of lists
emp_df = pd.DataFrame(emp_data, columns=["Name", "Sales", "Department", "Dept_ID"])
dept_df=pd.DataFrame({
    "Dept_ID": [1, 2, 3, 4],
    "Name": ["Sales", "Marketing", "Finance", "IT"],
    "Manager": ["Eve", "Frank", "Grace", "Harry"]
})
print(emp_df.groupby('Department').Sales.nlargest(2))
joined_df=pd.merge(dept_df,emp_df,how="left",left_on='Dept_ID',right_on='Dept_ID')
print(joined_df['Name_x'])
#print(joined_df[['Dept_Name','Name']].rename(columns={'Dept_Name':'Department'}))