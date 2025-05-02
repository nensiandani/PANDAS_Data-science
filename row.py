# head() , tail()
#head() 5
#tail(n) 5

import pandas as pd 

df = pd.read_json("D:\Data Science\PANDAS\sample_Data.json")

print('Display 10 row of first')
print(df.head())

print('Display 10 row of last')
print(df.tail())