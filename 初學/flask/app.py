from flask import Flask
app=Flask(__name__)    #__name__ 代表目前執行的模組

@app.route("/")    #函式的裝飾(Decotator):以函式為基礎,提供附加功能
def home():
	return "Hello Flask in /"

@app.route("/test")    #函式的裝飾(Decotator):以函式為基礎,提供附加功能
def test():
	return "This is test"

if __name__ =="__main__":    #如果以主程式執行
	app.run()    #立刻啟動伺服器
