import pandas as pd
import numpy as np

# Step 1: Create the DataFrame
data = {
    'OrderID': [101, 102, 103, 104, 105],
    'Product': ['Laptop', 'Headphones', 'T-shirt', 'Book', 'Shoes'],
    'Category': ['Electronics', 'Electronics', 'Clothing', 'Stationery', 'Footwear'],
    'Price': [70000, 2000, 500, 300, 2500],
    'Quantity': [1, 2, 3, 5, 1]
}

df = pd.DataFrame(data)

print("📋 Original Sales Data:")
print(df)

# Step 2: Add a new column: Total Price
df['TotalPrice'] = df['Price'] * df['Quantity']

print("\n💰 Sales Data with Total Price:")
print(df)

# Step 3: Calculate overall statistics using NumPy
mean_price = np.mean(df['Price'])
std_price = np.std(df['Price'])
total_revenue = np.sum(df['TotalPrice'])

print(f"\n📊 Mean Product Price: ₹{mean_price:.2f}")
print(f"📉 Standard Deviation of Price: ₹{std_price:.2f}")
print(f"💵 Total Revenue: ₹{total_revenue}")

# Step 4: Find the most expensive product
most_expensive = df.loc[df['Price'].idxmax(), 'Product']

print(f"\n🏆 Most Expensive Product: {most_expensive}")

# Step 5: Group by Category and calculate total revenue per category
category_revenue = df.groupby('Category')['TotalPrice'].sum()

print("\n📂 Revenue by Category:")
print(category_revenue)


'''
📋 Original Sales Data:
   OrderID     Product     Category  Price  Quantity
0      101      Laptop  Electronics  70000         1
1      102  Headphones  Electronics   2000         2
2      103     T-shirt     Clothing    500         3
3      104        Book   Stationery    300         5
4      105       Shoes     Footwear   2500         1

💰 Sales Data with Total Price:
   OrderID     Product     Category  Price  Quantity  TotalPrice
0      101      Laptop  Electronics  70000         1       70000
1      102  Headphones  Electronics   2000         2        4000
2      103     T-shirt     Clothing    500         3        1500
3      104        Book   Stationery    300         5        1500
4      105       Shoes     Footwear   2500         1        2500

📊 Mean Product Price: ₹15060.00
📉 Standard Deviation of Price: ₹27482.98
💵 Total Revenue: ₹79500

🏆 Most Expensive Product: Laptop

📂 Revenue by Category:
Category
Clothing        1500
Electronics    74000
Footwear        2500
Stationery      1500
Name: TotalPrice, dtype: int64

'''