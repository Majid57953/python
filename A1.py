import random
import pandas as pd
from datetime import datetime
class EmployeeClass:
    def __init__(self,name,surname,age) :
        self.name=name
        self.surname=surname
        self.age=age  
#List of Employee
itemCount=[]
EmployeeDict={
    'Id':[1,2],
    'Name':
    ['Iten','Clara'],
    'Surname':
    ['Hunt','McDowel']
    }
for i in EmployeeDict["Name"]:
    cc=random.randint(1,10)
    #print('Today {} created {} phones'.format(i,cc))
    itemCount.append(cc)
dataDict={
    'Id':EmployeeDict['Id'],
    'Name':EmployeeDict['Name'],
    'Surname':EmployeeDict['Surname'],
    'Count':itemCount
}
df=pd.DataFrame(dataDict)

#Gets the current datekey with seconds
def GetCurrentDK(): 
    return datetime.now().strftime('%Y%m%d%H%M%S')
#Opens the file or creates a file
def CreateFile (): 
    # file=open('{}.txt'.format(GetCurrentDK()),'w') 
    # file.write('Name,ItemCount')
    # for i in EmployeeDict:
    #     cc=random.randint(1,10)
    #     file.write('\n{},{}'.format(i,cc))
    # file.close()
    df.to_csv(GetCurrentDK()+'.txt',index=None)
# print(GetCurrentDK())
CreateFile()

