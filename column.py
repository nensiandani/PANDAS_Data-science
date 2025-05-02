import pandas as pd 

data = {
    "name" : ["nenu","yashu","anu","ridhu","jex","piyu"],
    "age" : [20,22,19,20,32,25],
    "salary" : [50000,650000,70000,45000,74000,55000],
    "parfromance score" : [85,95,69,78,88,90]
 }

df = pd.DataFrame(data)

print(df['name'])

subset = df[['name' , 'salary']]
print('subset with name and age')
print(subset)


'''
0     nenu
1    yashu
2      anu
3    ridhu
4      jex
5     piyu
Name: name, dtype: object
subset with name and age
    name  salary
0   nenu   50000
1  yashu  650000
2    anu   70000
3  ridhu   45000
4    jex   74000
5   piyu   55000

'''