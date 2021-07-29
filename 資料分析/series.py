import pandas as pd
#建立一個series
data=pd.Series([50,10,15,3,-10,-20,40],index=["a","b","c","d","e","f","g"])#內建index為0,1,2,3....
print(data)
print("\n")
print("資料型態 ",data.dtype)
print("\n")
print("資量數量 ",data.size)
print("\n")
print("資料索引 ",data.index)
print("\n")

print(data[2],data[0]) #根據順序
print("\n")
print(data["e"],data["b"]) #根據索引
print("\n")

print("最大值 ",data.max())
print("\n")
print("總和 ",data.sum())
print("\n")
print("標準差 ",data.std())
print("\n")
print("中位數 ",data.median())
print("\n")
print("最大三個數\n",data.nlargest(3))
print("最小兩個數\n",data.nsmallest(2))
print("\n")


data=pd.Series(["你好","Python","Hello"])
print(data)
print("\n")
print(data.str.lower())
print("\n")
print(data.str.len())
print("\n")
print(data.str.cat(sep="+"))
print("\n")
print(data.str.contains("P"))#判斷字串否包含P
print("\n")
print(data.str.replace("你好","Guten Tag"))
print("\n")
