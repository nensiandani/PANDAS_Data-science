'''

df["column name"].mean()
df["column name].min()
df["column name].max()
df["column name].sum()

'''


import pandas as pd 

data = {
    "name" : ["nensi", "yashi", "anandi"],
    "age" : [22,34,28],
    "salary" : [20000,40000,30000]

}

df = pd.DataFrame(data)

avg_salary = df['salary'].mean()
print(avg_salary)
 

 '''
 30000.0
 '''
