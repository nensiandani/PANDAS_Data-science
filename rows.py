import pandas as pd 

data = {
    "name" : ["nenu","yashu","anu","ridhu","jex","piyu"],
    "age" : [20,22,19,20,32,25],
    "salary" : [50000,650000,70000,45000,74000,55000],
    "parfromance_score" : [85,95,69,78,88,90]
 }

df = pd.DataFrame(data)

high_salary = df[df['salary'] > 50000]
print("employee hight salary > 50000 ")
print(high_salary)

filtter = df[(df['age'] > 20) & (df['salary'] > 50000)]
print("employee list age > 30 + salary >50000")
print(filtter)

filtter_or = df[(df['age'] > 25) | (df['parfromance_score'] > 90)]
print("employee older 25 and parformace > 90")
print(filtter_or)

'''
employee hight salary > 50000 
    name  age  salary  parfromance_score
1  yashu   22  650000                 95
2    anu   19   70000                 69
4    jex   32   74000                 88
5   piyu   25   55000                 90
employee list age > 30 + salary >50000
    name  age  salary  parfromance_score
1  yashu   22  650000                 95
4    jex   32   74000                 88
5   piyu   25   55000                 90
employee older 25 and parformace > 90
    name  age  salary  parfromance_score
1  yashu   22  650000                 95
4    jex   32   74000                 88

'''