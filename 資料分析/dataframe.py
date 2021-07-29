import pandas as pd
#建立Dataframe:pd.DataFrame(字典,index=索引)
data=pd.DataFrame({
	"name":["Amy","John","Bob"],
	"age":[20,45,38],
	"salary":[30000,50000,40000]
} , index=["a","b","c"])

print(data)
print("====================")
print("資料數量",data.size)
print("資料形狀(列,欄)",data.shape)
print("資料索引",data.index)
print("====================")
#取得row
print("取得第二列",data.iloc[1],sep="\n")
print("====================")
print("取得第c列",data.loc["c"],sep="\n")
print("====================")
#取得column相當於一維的series
print("取得name欄位",data["name"],sep="\n")
print("====================")
#轉成series
salaries=data["salary"]
print("薪水平均值",salaries.mean())
print("====================")
#建立新欄位data[新增欄位]=列表
data["revenue"]=[5000000,4000000,3000000]
data["rank"]=pd.Series([3,6,1],index=["a","b","c"])#data[新欄位的名稱]=Series的資料
print(data)
print("====================")
data["cp"]=data["revenue"]/data["salary"]
print(data)
