import numpy as np
#一維
array=np.array([3,4,5])
print(array)
array=np.empty(4) #創造一個有四個資料的一維陣列，資料未指定
print(array)
array=np.zeros(3)
print(array)
array=np.ones(5)
print(array)
array=np.arange(10)
print(array)

#二維
array=np.array([[1,2,3],[2,3,4]])
print(array)
print(array.size)

#三維
array=np.array([
	[
		[1,2,3],[4,5,6],[7,8,9]
	],
	[
		[10,11,12],[13,14,15],[16,17,18]
	],
	[
		[19,20,21],[22,23,24],[25,26,27]
	]
])
print(array)
array=np.zeros([3,2,3])
print(array)


