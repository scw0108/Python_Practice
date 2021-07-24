#抓取ajax網頁原始碼
import urllib.request as req
url="https://www.kkday.com/zh-tw/home/ajax_get_homepage_setting?csrf_token_name=510eb1f24fe3e47cc19d313e0e360f4c"
#建立一個request物件，附加request headers的資訊
request=req.Request(url, headers={ "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"})

with req.urlopen(request) as response:
	data=response.read().decode("utf-8")

#解析json格式的資，取得每篇文章標題
import json
data=json.loads(data)
post=data["data"]["top_products"]["prod_list"]
for key in range(0,10):
	posts=post[key]
	with open ("kkday.txt",mode="a",encoding="utf-8") as file:
		file.write(posts["name"]+"\n")

