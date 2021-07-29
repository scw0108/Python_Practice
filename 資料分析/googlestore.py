import pandas as pd
data=pd.read_csv("googleplaystore.csv")

print("資料欄位",data.columns,sep="\n")
print("====================")
print("row x column",data.shape,sep="\n")
print("====================")

print("分析資料---評分的各種統計數據=>")
condition=data["Rating"]<=5
data=data[condition]
print("平均數: ",data["Rating"].mean())
print("中位數: ",data["Rating"].median())
print("取得前一千個應用程式的平均: ",data["Rating"].nlargest(1000).mean())
print("====================")

print("分析資料---安裝數量的各種統計=>")
print(data["Installs"])
data["Installs"]=data["Installs"].str.replace("[+,]","").replace("Free","")

data["Installs"]=pd.to_numeric(data["Installs"])
#將Installs中字串轉數字並替換掉特殊符號
print("平均數: ",data["Installs"].mean())
condition=data["Installs"]>100000
print("安裝數量大於10000 ",data[condition].shape)

