import pandas as pd
student_data=[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20],
  [5,21]
]
empty_data=[
  [1,'Wayne'],
  [2,'John'],
  [3,'Tereza'],
  [4,'Bale'],
  [5,]]

empty_data2=[
    [6,'Grace']
]

dfmerge=pd.DataFrame({'Id':[1,2,3],'Name':["Bob", "Charlie", "David"]})
dfmerge2=pd.DataFrame({'Id':[1,2],'position':["CEO", "CTO"]})
dfpivot = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "Gender": ["F", "M", "M", "M", "F", "M"],
    "Age": [25, 30, 35, 40, 45, 50],
    "Salary": [4000, 5000, 6000, 7000, 8000, 9000],
    "Department": ["IT", "HR", "Sales", "Marketing", "Finance", "Legal"]
})

dfmelt = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "Gender": ["F", "M", "M", "M", "F", "M"],
    "Age": [25, 30, 35, 40, 45, 50],
    "Salary": [4000, 5000, 6000, 7000, 8000, 9000],
    "Department": ["IT", "HR", "Sales", "Marketing", "Finance", "Legal"]
})



df2=pd.DataFrame(empty_data,columns=['Id','Name'])
df3=pd.DataFrame(empty_data2,columns=['Id','Name'])
def createDataframe(student_data) -> pd.DataFrame:
    return pd.DataFrame(student_data,columns=['student_id','name'])
df=createDataframe(student_data)
print(createDataframe(student_data))


def getDataframeSize(players: pd.DataFrame)->list[int]:
    return list(players.shape)
print(getDataframeSize(df))

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    #return employees.assign(salary=employees['name']*2)
    employees['bonus']=employees['name']*2
    return employees

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset='name',keep='last')
# def retColumns(players)->pd.DataFrame:
#     return players[(players['student_id']==3)][['student_id']]

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset='Name')

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['Id']=employees['Id']*2
    employees.Id=employees.Id*2
    employees['Id']=employees['Id'].apply(lambda x:x*2)
    return employees

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.columns=['IdM','NameM']
    return students

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    #return students.astype({'Id':float})
    students['Id']=students['Id'].astype(float)
    return students

def fillMissingValues(students:pd.DataFrame)->pd.DataFrame:
    students['Name'].fillna(0,inplace=True)
    return students
    #return students.fillna({'Id':0})

def concatenateTables(dfx: pd.DataFrame, dfy: pd.DataFrame) -> pd.DataFrame:
    #return pd.concat([dfx,dfy],axis=1)
    return pd.concat([dfx,dfy])

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return pd.pivot_table(weather,values='Salary',index='Gender',columns='Department',aggfunc='mean',fill_value=0)

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report,id_vars='Gender',value_vars=['Finance','HR'],var_name='Attribute',value_name='Value')
#print(dfmelt)
#dfmelt2=pivotTable(dfpivot)
#print(df[df['name']>15].sort_values(by='name',ascending=False)['name'])

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    #df=pd.merge(person,address,how="left",on='Id')
    #return df[['Name','position']]
    return pd.merge(person,address,how="left",on='Id')[['Name','position']]

#print(combine_two_tables(dfmerge,dfmerge2))

#df['bonus']=df['name'].where((df['name']%2==0) & (df['student_id']!=4))
print(df2[df2['Name'].str.contains('John',na=False)])
print(df2)



