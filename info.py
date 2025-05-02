import pandas as pd 

df = pd.read_json("D:\Data Science\PANDAS\sample_Data.json")

print('display the info of data set')
print(df.info())