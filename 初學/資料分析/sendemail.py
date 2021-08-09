import email.message
msg=email.message.EmailMessage()

msg["From"]="109703042@g.nccu.edu.tw"
msg["To"]="bruce900108@hotmail.com"
msg["Subject"]="Hello"

#寄送純文字內容
msg.set_content("測試python傳送")
#寄送比較多樣式的內容(html)
#msg.add_alternative("<h3>優惠券</h3>滿五百送一百喔",subtype="html")

#連線到SMTP Server,驗證寄件人身份並發送郵件
import smtplib
#Google smtp server
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("帳號","密碼")
server.send_message(msg)
server.close()
