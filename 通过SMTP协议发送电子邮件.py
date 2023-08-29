import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 发件人和收件人的电子邮件地址
fro_add = "dilipvijjapu@gmail.com"
to_add = "vijjapudilip@gmail.com"

# 创建一个MIMEMultipart对象
message = MIMEMultipart()
message["From"] = fro_add
message["To"] = ",".join(to_add)
message["Subject"] = "Testing mail"

# 邮件正文
body = "嗨，我是Dilip，你好吗？"
message.attach(MIMEText(body, "plain"))

# 发送邮件的邮箱和密码
email = "your_email@gmail.com"
password = "your_password"

# 连接到Gmail的SMTP服务器
mail = smtplib.SMTP("smtp.gmail.com", 587)
mail.ehlo()
mail.starttls()
mail.login(email, password)

# 将消息转换为字符串并发送邮件
text = message.as_string()
mail.sendmail(fro_add, to_add, text)

# 关闭连接
mail.quit()
