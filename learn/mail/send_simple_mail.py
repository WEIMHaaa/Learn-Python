import smtplib
from email.mime.text import MIMEText

# 发送者邮箱地址
senderMail = '1425615649@qq.com'
# 发送者 QQ 邮箱授权码
authCode = 'ervqgaxvcgzaieib'
# 接收者邮箱地址
receiverMail = '1010293890@qq.com'
# 邮件主题
subject = '简单邮件'
# 邮件内容
content = 'hello email'
msg = MIMEText(content, 'plain', 'utf-8')
msg['Subject'] = subject
msg['From'] = senderMail
msg['To'] = receiverMail
try:
    server = smtplib.SMTP_SSL('smtp.qq.com', smtplib.SMTP_SSL_PORT)
    print('成功连接到邮件服务器')
    server.login(senderMail, authCode)
    print('成功登录邮箱')
    server.sendmail(senderMail, receiverMail, msg.as_string())
    print('邮件发送成功')
except smtplib.SMTPException as e:
    print('邮件发送异常')
finally:
    server.quit()