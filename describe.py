import pandas as pd 

data = {
    "name" : ["nenu","yashu","anu","ridhu","jex","piyu"],
    "age" : [20,22,19,20,32,25],
    "salary" : [50000,650000,70000,45000,74000,55000],
    "parfromance score" : [85,95,69,78,88,90]
 }

df = pd.DataFrame(data)
print(df)

print("descriptive statistics")
print(df.describe())

 
'''
 name  age  salary  parfromance score
0   nenu   20   50000                 85
1  yashu   22  650000                 95
2    anu   19   70000                 69
3  ridhu   20   45000                 78
4    jex   32   74000                 88
5   piyu   25   55000                 90
descriptive statistics
             age         salary  parfromance score
count   6.000000       6.000000           6.000000
mean   23.000000  157333.333333          84.166667
std     4.898979  241620.915209           9.325592
min    19.000000   45000.000000          69.000000
25%    20.000000   51250.000000          79.750000
50%    21.000000   62500.000000          86.500000
75%    24.250000   73000.000000          89.500000
max    32.000000  650000.000000          95.000000

'''