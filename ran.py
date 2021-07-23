import random 

data=random.choice([0,1,5,8,4]) # 隨機選取
print(data)

data=random.sample([1,2,4,6,10,9],3) #隨機選取三個
print(data)

data=[1,2,3,4,5,6]
random.shuffle(data) #隨機調換順序
print(data)

data=random.random() #0.0~1.0隨機選取
print(data)

data=random.uniform(60,100) #60~100隨機選取
print(int(data))

data=random.normalvariate(70,30) #取得常態分配亂數平均數70標準差30
print(data)

import statistics as stat #統計模組

data=stat.mean([1,4,5,8]) #平均數
print(data)

data=stat.median([1,1,1,1,1,5,9,10,5]) #中位數
print(data)

data=stat.stdev([12,15,1,1,1,5,9,10,5,2,8,7]) #標準差
print(data)
