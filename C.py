x=input()
y=input()
x=int(x)
y=int(y)


def P(x):
	sum=1
	for x in range(2,x+1):
		sum*=x
	return sum

def ccc(n1,n2):
	return P(n1)/(P(n2)*P(n1-n2))
print(int(ccc(n2=y,n1=x)))
	

