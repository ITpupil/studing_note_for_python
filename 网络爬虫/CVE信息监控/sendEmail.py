import smtplib
from email.mime.text import MIMEText
from email.header import Header
import base64
import pysnooper

from config import HOST,USER,LICENSE_CODE,SENDER,RECEIVERS,SENDER_INFO,SUBJECT,CVE_HTML

class sendCveEmail(object):
    def __init__(self, cves):
        self.cves=cves
        self.server = smtplib.SMTP() 
        self.server.connect(HOST)
        self.server.login(USER,LICENSE_CODE)
        self.send()

    def pressData(self):
        cve_info=""
        for cve in self.cves:
            cve_info += f"<tr><th>{cve[0]}</th><th>{self.outBase64(cve[1])}</th><th>{cve[2]}</th><th>{self.outBase64(cve[3])}</th></tr>"
        return CVE_HTML.format(cve_info)

    def outBase64(self,base64_string):
        return base64.b64decode(base64_string)

    def send(self):
        message = MIMEText(self.pressData(), 'html', 'utf-8')
        message['From'] = SENDER_INFO
        message['To'] = ','.join(RECEIVERS)
        message['Subject'] = Header(SUBJECT, 'utf-8')
        self.server.sendmail(SENDER,RECEIVERS,message.as_string())
        print('邮件发送完成')

        # try:
        #     message = MIMEText(self.pressData(), 'html', 'utf-8')
        #     message['From'] = SENDER_INFO
        #     message['To'] = ','.join(RECEIVERS)
        #     message['Subject'] = Header(SUBJECT, 'utf-8')
        #     self.server.sendmail(SENDER,RECEIVERS,message.as_string())
        #     print('邮件发送完成')
        # except Exception as e:
        #     print('邮件发送失败：',e)
        # finally:
        #     self.server.quit()

cves=(["b'MTIxMjEz'","b'MTIxMjEz'","b'MTIxMjEz'","b'MTIxMjEz'"],["b'MTIxMjEz'","b'MTIxMjEz'","b'MTIxMjEz'","b'MTIxMjEz'"])

sendCveEmail(cves)

# 未完成，编译报错