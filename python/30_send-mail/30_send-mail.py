# 準備訊息物件設定
import email.message

msg = email.message.EmailMessage()
msg["From"] = "寄件人"
msg["To"] = "收件人"
msg["Subject"] = "你好"
# 寄送純文字內容
msg.set_content("測試看看")

# 寄送比較多樣式的內容(html)

# msg.add_alternative("<h3>優惠券</h3>滿五百送一百哦", subtype="html")

# 連線到 SMTP Server，驗證寄件人身份並發送郵件
import smtplib

# 上網搜尋 gmail smtp sever
sever = smtplib.SMPT_SSL("smtp.gmail.com", 465)
sever.login("帳號", "密碼")
sever.send_message(msg)
sever.close()