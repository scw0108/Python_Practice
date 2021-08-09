a=[1,5,6,3,4,9,7]
for i in range(7):
	for j in range(7):
		print("i=",i,",j=",j,sep=" ") 
		if a[i]<a[j]:
			temp=a[j]
			a[j]=a[i]
			a[i]=temp
for i in range(7):
	print(a[i])



