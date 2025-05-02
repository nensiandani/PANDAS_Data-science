import pandas as pd
import numpy as np

# Dataset
data = {
    'OrderID': [201, 202, 203, 204],
    'Customer': ['John', 'Anna', 'Mike', 'Sara'],
    'Amount': [2500, 3000, 1500, 4000],
    'Items': [2, 3, 1, 4]
}

df = pd.DataFrame(data)

# Add a new column: Price per Item
df['PricePerItem'] = df['Amount'] / df['Items']

# Find total sales
total_sales = np.sum(df['Amount'])

# Find customer who spent most
top_spender = df.loc[df['Amount'].idxmax(), 'Customer']

print(df)
print(f"\n💵 Total Sales: ₹{total_sales}")
print(f"🏆 Top Spender: {top_spender}")


'''
 OrderID Customer  Amount  Items  PricePerItem
0      201     John    2500      2        1250.0
1      202     Anna    3000      3        1000.0
2      203     Mike    1500      1        1500.0
3      204     Sara    4000      4        1000.0

💵 Total Sales: ₹11000
🏆 Top Spender: Sara

'''