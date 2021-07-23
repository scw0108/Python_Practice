class file:
	def __init__(self,name):
		self.name=name
		self.file=None
	def open(self):
  		self.file=open(self.name,mode="r",encoding="utf-8")
	def read(self):
		return self.file.read()

	def open2(self):
		with open(self.name,mode="r",encoding="utf-8") as data:
			result=data.read()
			print(result)


f1=file("data1.txt")
f1.open()
data=f1.read()
print(data)

f2=file("data2.txt")
f2.open2()
