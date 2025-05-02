
import pandas as pd
import numpy as np

# Food delivery data
data = {
    'OrderID': [301, 302, 303],
    'Restaurant': ['Dominos', 'KFC', 'McDonalds'],
    'DeliveryTime': [30, 45, 25],  # in minutes
    'OrderAmount': [500, 700, 450]
}

df = pd.DataFrame(data)

# Delivery speed categories
df['DeliverySpeed'] = np.where(df['DeliveryTime'] <= 30, 'Fast', 'Slow')

# Calculate average order amount
avg_order = np.mean(df['OrderAmount'])

print("🍕 Food Delivery Orders:")
print(df)
print(f"\n🍽️ Average Order Amount: ₹{avg_order}")


'''
🍕 Food Delivery Orders:
   OrderID Restaurant  DeliveryTime  OrderAmount DeliverySpeed
0      301    Dominos            30          500          Fast
1      302        KFC            45          700          Slow
2      303  McDonalds            25          450          Fast

🍽️ Average Order Amount: ₹550.0
'''