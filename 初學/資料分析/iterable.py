#可疊代Iterable : 可以分開逐一取出的資料
#for 變數名稱 in 可疊代資料：
for x in "abc":
	print(x)
for x in {"a,","test",3,10}:
	print(x)
dic={"c":3,"a":5}
for x in dic:
	print(x)
	print(dic[x])

result=max([10,2,5,40,1])
print(result)
result=sorted([10,2,5,40,1])
print(result)
result=sorted(dic)
print(result)
