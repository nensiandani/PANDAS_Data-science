import pandas as pd 

data = {
    "name" : ["nenu","yashu","anu","ridhu","jex","piyu"],
    "age" : [20,22,19,20,32,25],
    "salary" : [50000,650000,70000,45000,74000,55000],
    "parfromance_score" : [85,95,69,78,88,90]
 }

df = pd.DataFrame(data)
print(df)

df['salary'] = df['salary'] * 1.05

print(df)


'''

name  age  salary  parfromance_score
0   nenu   20   50000                 85
1  yashu   22  650000                 95
2    anu   19   70000                 69
3  ridhu   20   45000                 78
4    jex   32   74000                 88
5   piyu   25   55000                 90


    name  age    salary  parfromance_score
0   nenu   20   52500.0                 85
1  yashu   22  682500.0                 95
2    anu   19   73500.0                 69
3  ridhu   20   47250.0                 78
4    jex   32   77700.0                 88
5   piyu   25   57750.0                 90


'''