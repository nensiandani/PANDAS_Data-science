import pandas as pd

# customer data 
df_customer = pd.DataFrame({
    "customerid" : [1,2,3,4],
    "name" : ["nensi", "yashi","anandi","jex"]
})

# order data 
df_order = pd.DataFrame({
    "customerid" : [1,2,3,5],
    "orderamount" :[290,300,450,430]
})

# marge data 

df_merg = pd.merge(df_customer,df_order, on="customerid" ,how="inner")  # how=outer

print(df_merg)


'''
  customerid    name  orderamount
0           1   nensi          290
1           2   yashi          300
2           3  anandi          450

'''