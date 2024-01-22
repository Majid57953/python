import pandas as pd
student_data=[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

def createDataframe(student_data) -> pd.DataFrame:
    return pd.DataFrame(student_data,columns=['student_id','name'])
df=createDataframe(student_data)
print(createDataframe(student_data))


def getDataframeSize(players: pd.DataFrame)->list[int]:
    return list(players.shape)
print(getDataframeSize(df))
