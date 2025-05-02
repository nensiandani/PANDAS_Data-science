# pd.concate([df1,df2] , axis=0 ,ignore_index=True)

# vertical
import pandas as pd 

df_region1 = pd.DataFrame({
    "id" : [1,2],
    "name" : ["nenu","yasu"]
})

df_region2 = pd.DataFrame({
     "id" : [3,4],
    "name" : ["nensi","yashi"]
})
    

#concatenation
df_con = pd.concat([df_region1,df_region2],axis=0,ignore_index=True)
print(df_con)

'''
  id   name
0   1   nenu
1   2   yasu
2   3  nensi
3   4  yashi

'''