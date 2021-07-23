#class 類別名稱: 
#	def __init__ (self): (定義初始化函數)
#		透過操作self來定義實體屬性

#建立實體物件，放入變數obj中
#obj=類別名稱()＃呼叫初始化函數

class point:
	def __init__(self,x,y):
		self.x=x
		self.y=y

p1=point(3,4)
print(p1.x,p1.y)

p2=point(5,6)
print(p2.x,p2.y)

