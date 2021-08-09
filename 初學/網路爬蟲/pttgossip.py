#抓取ptt gossip的網頁原始碼
import urllib.request as req

def getData(url):
	#建立一個request物件，附加request headers的資訊包含cookie
	request=req.Request(url, headers={ 
		"cookie":"over18=1",
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"})

	with req.urlopen(request) as response:
		data=response.read().decode("utf-8")
	#print(data)

	#解析原始碼，取得每篇文章標題
	import bs4
	root=bs4.BeautifulSoup(data,"html.parser")
	titles=root.find_all("div",class_="title") #尋找class="title"的div標籤

	for title in titles:
		if title.a!=None: #如果標題有包含a標籤
			print(title.a.string)
			with open ("pttgossip.txt",mode="a",encoding="utf-8") as file:
				for data in title.a:
					file.write(data+"\n")
	with open ("pttgossip.txt",mode="a",encoding="utf-8") as file:
		file.write("\n")

	nextLink=root.find("a",string="‹ 上頁") #抓取多個頁面的連結
	print("\n")
	return nextLink["href"]


pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count =0
while count<3:
	pageURL="https://www.ptt.cc/"+getData(pageURL)
	count+=1




