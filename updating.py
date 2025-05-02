import pandas as pd 

data = {
    "name" : ["nenu","yashu","anu","ridhu","jex","piyu"],
    "age" : [20,22,19,20,32,25],
    "salary" : [50000,650000,70000,45000,74000,55000],
    "parfromance_score" : [85,95,69,78,88,90]
 }

df = pd.DataFrame(data)


# .loc
#df.loc[row_index , "column name" ] =   new_data

df.loc[1,"parfromance_score"] = 55
print(df)

'''
 name  age  salary  parfromance_score
0   nenu   20   50000                 85
1  yashu   22  650000                 55
2    anu   19   70000                 69
3  ridhu   20   45000                 78
4    jex   32   74000                 88
5   piyu   25   55000                 90

'''