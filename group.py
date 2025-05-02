
import pandas as pd 

data = {
    "name" : ["nensi", "yashi", "anandi","jex","janu"],
    "age" : [22,34,28,34,22],
    "salary" : [20000,40000,30000,45000,23000]

}

df = pd.DataFrame(data)

grouped = df.groupby("age")["salary"].sum()
print(grouped) 

'''
age
22    43000
28    30000
34    85000


22    20000+23000  =  43000
28    30000
34    40000+45000   =  85000

'''