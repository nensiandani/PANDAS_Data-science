import pandas as pd 

data = {
    "name" : ["nensi","yashvi","anandi"],
    "age" : [20,25,30],
    "city" : ["latipar","manvadaer","jasdad"]
}

df = pd.DataFrame(data)

print(df)

#df.to_csv("output.csv")   #index=False 0,1,2,3...

#df.to_excel("output.xlsx" , index=False)  

df.to_json("output.json" , index=False)

'''
 name  age       city
0   nensi   20    latipar
1  yashvi   25  manvadaer
2  anandi   30     jasdad

'''