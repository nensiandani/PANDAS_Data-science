import numpy as np
import pandas as pd 

# Bank transactions dataset
data = {
    'Customer': ['C1', 'C2', 'C3', 'C4'],
    'Deposit': [10000, 15000, 12000, 11000],
    'Withdraw': [2000, 3000, 1000, 500]
}

df = pd.DataFrame(data)

# Net Balance
df['Balance'] = df['Deposit'] - df['Withdraw']

# Mean Balance
mean_balance = np.mean(df['Balance'])

print("🏦 Bank Transactions:")
print(df)
print(f"\n💰 Average Customer Balance: ₹{mean_balance}")


'''
🏦 Bank Transactions:
  Customer  Deposit  Withdraw  Balance
0       C1    10000      2000     8000
1       C2    15000      3000    12000
2       C3    12000      1000    11000
3       C4    11000       500    10500

💰 Average Customer Balance: ₹10375.0
'''