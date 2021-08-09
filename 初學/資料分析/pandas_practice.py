import pandas as pd
#建立一個series
data=pd.Series([50,10,15])

#print(data.max())#最大值
#print(data.median())#中位數
#data=data*2
#print(data)
#data=data==10#比較有沒有等於10
#print(data)

#建立Dataframe
data=pd.DataFrame({
	"name":["Amy","John","Bob"],
	"salary":[30000,50000,40000]
})
print(data)
print("====================")
print(data["salary"])#印出印出column
print("====================")
print(data.iloc[0])#印出第一row
