#網路連接
import urllib.request as request
src="https://www.ntu.edu.tw/"
with request.urlopen(src) as response:
	data=response.read().decode("utf-8")#取得台灣大學原始碼
#print(data)

#台北市公開資料
import urllib.request as request
import json
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
	data=json.load(response)
#將公司名稱列表出來
clist=data["result"]["results"]
with open("company.txt","w",encoding="utf-8") as file:
	for company in clist:
		file.write(company["公司名稱"]+"\n")

with open("stock.json",mode="r",encoding="utf-8") as file:
	data=json.load(file)

with open("stock.txt","w",encoding="utf-8") as file:
	for stock in data:
		file.write(stock["證券代號"]+" "+stock["證券名稱"]+" "+stock["成交股數"]+" "+stock["成交金額"]+" "+stock["開盤價"]+" "+stock["最高價"]+" "+stock["最低價"]+" "+stock["收盤價"]+"\n")
