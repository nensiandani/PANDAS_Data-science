'''

Method	   Meaning

'linear'	   Straight line interpolation (default)
'polynomial'	Interpolate using a polynomial curve
'time'	        Time-based interpolation (for time series)
'nearest'	    Use nearest known value
'spline'	    Spline interpolation (smooth curves)

'''


import pandas as pd
import numpy as np

data = {'A': [1, np.nan, np.nan, 4, 5]}
df = pd.DataFrame(data)

# Polynomial interpolation (degree=2)
df_poly = df.interpolate(method='polynomial', order=2)

print(df_poly)


'''
Before:
     A
0  1.0
1  2.0
2  NaN
3  4.0
4  5.0

After:
     A
0  1.0
1  2.0
2  3.0
3  4.0
4  5.0
'''