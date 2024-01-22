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

df2=pd.DataFrame(empty_data,columns=['Id','Name'])
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

print(fillMissingValues(df2))

