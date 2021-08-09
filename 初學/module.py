import sys
sys.path.append("./modules") #在模組的搜尋路經『新增路徑』
import geometry as ge

result=ge.distance(1,1,5,5)
print(result)
result=ge.slope(1,6,9,4);
print(result)

print(sys.path) #印出模組搜尋路徑
