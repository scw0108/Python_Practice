class Fullname:
	def __init__(self,first,last):
		self.first=first
		self.last=last
	def printname(self):  #定義實體函數與方法(def 名稱 (self,更多參數)) 
		print("Your name is",self.first,self.last)
	def BMI(self,heigh,weigh):
		print((weigh)/((heigh/100)**2))

name=Fullname("Sun","Chun-wei") 
name.printname()
name.BMI(180,60)
