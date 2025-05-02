import pandas as pd

data = {
    "time" : [1,2,3,4,5,6],
    "value" : [10,None,30,40,None,60]

}

df=pd.DataFrame(data)
print("Before interpolate")
print(df)

df['value'] = df['value'].interpolate(method='linear')

print("After interpolate")
print(df)

'''
Before interpolate
   time  value
0     1   10.0
1     2    NaN
2     3   30.0
3     4   40.0
4     5    NaN
5     6   60.0
After interpolate
   time  value
0     1   10.0
1     2   20.0
2     3   30.0
3     4   40.0
4     5   50.0
5     6   60.0

'''