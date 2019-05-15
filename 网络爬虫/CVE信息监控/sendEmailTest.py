import smtplib
from email.mime.text import MIMEText
from email.header import Header
import pysnooper


# 第三方 SMTP 服务
host="smtp.qq.com"  #设置服务器
user="邮箱账户@qq.com"    #用户名
password="*************"   #邮箱授权码 

sender = '邮箱账户@qq.com' #发送邮件的账户
receivers = ['邮箱账户@qq.com','邮箱账户@qq.com']  # 接收邮件的账户

message = MIMEText('Python 邮件发送测试...（这里为邮件内容）', 'plain', 'utf-8')
message['From'] = "CVE监控脚本"
message['To'] = ','.join(receivers)
# message['From'] = Header("发送人的姓名（或备注）", 'utf-8') 
# message['To'] =  Header("收件人的姓名（或备注）", 'utf-8') #不会显示收件人信息
 
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    server = smtplib.SMTP() 
    server.connect(host)    # 25 为 SMTP 端口号
    server.login(user,password)
    server.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")