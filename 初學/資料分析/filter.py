import pandas as pd
data=pd.Series([30,15,20])
#資料篩選
condition1=[True,False,True]
print(data[condition1])
print("====================")

condition2=data<30
print(data[condition2])
print("====================")

data=pd.Series(["你好","Python","Pandas"])
condition=data.str.contains("P")
print(data[condition])
print("====================")

data=pd.DataFrame({
	"name":["Amy","John","Bob"],
	"salary":[60000,50000,40000]
})

condition=[False,True,True]
print(data[condition])
print("====================")

condition=data["salary"]>=50000
print(data[condition])
print("====================")

condition=data["name"]=="Amy"
print(data[condition])
print("====================")

