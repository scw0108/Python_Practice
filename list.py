data=[1,2,3,4,5,6]
data[1:4]=[]
print(data[1])
data=(1,2,3,4,5)
data[1:3]=() #error tuple can not change 
print(data)
