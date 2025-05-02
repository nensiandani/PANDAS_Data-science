import pandas as pd 

data = {
    "name" : ["nenu","yashu",None,"ridhu","jex","piyu"],
    "age" : [20,22,None,20,32,25],
    "salary" : [50000,650000,None,45000,74000,55000],
    "parfromance_score" : [85,95,None,78,88,90]
 }

df = pd.DataFrame(data)
print(df)

df['age'].fillna(df['age'].mean(), inplace=True)
df['salary'].fillna(df['salary'].mean(), inplace=True)
df['parfromance_score'].fillna(df['parfromance_score'].mean(),inplace=True)

print(df)

'''
  name   age    salary  parfromance_score
0   nenu  20.0   50000.0               85.0
1  yashu  22.0  650000.0               95.0
2   None  23.8  174800.0               87.2
3  ridhu  20.0   45000.0               78.0
4    jex  32.0   74000.0               88.0
5   piyu  25.0   55000.0               90.0

'''