import random
import pandas as pd
import os
import glob
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
    cc=random.randint(1,2)
    #print('Today {} created {} phones'.format(i,cc))
    itemCount.append(cc)
dataDict={
    'Id':EmployeeDict['Id'],
    'Name':EmployeeDict['Name'],
    'Surname':EmployeeDict['Surname'],
    'Count':itemCount
}
df=pd.DataFrame(dataDict)

#Gets the current datekey
def GetCurrentDK(): 
    return datetime.now().strftime('%Y%m%d')
#Gets the current datekey with seconds
def GetCurrentDKT(): 
    return datetime.now().strftime('%Y%m%d%H%M%S')

#Opens the file or creates a file
def CreateFile (): 
    folder=str(GetCurrentDK())
    if not os.path.exists(folder):
        os.makedirs(folder)
    df.to_csv(folder+'/'+GetCurrentDKT()+'.txt',index=None)

def ShowStock():
    csv_file=glob.glob(os.path.join(GetCurrentDK(),'*.txt'))
    df2=pd.concat((pd.read_csv(f) for f in csv_file),ignore_index=True)
    print("Piece of Wood: {}".format(df2['Count'].sum()))

ShowStock()
