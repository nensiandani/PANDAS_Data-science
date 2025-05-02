# sorting data
# a b c d
# df.sort_value(by="column name" , true/false , inplace= true)

import pandas as pd 

data = {
    "name" : ["nensi", "yashi", "anandi"],
    "age" : [22,34,28]

}

df = pd.DataFrame(data)
print("not sort")
print(df)

df.sort_values(by="age",ascending=False , inplace=True)
print ("sort value")

print(df)


'''
not sort
     name  age
0   nensi   22
1   yashi   34
2  anandi   28
sort value
     name  age
1   yashi   34
2  anandi   28
0   nensi   22

'''