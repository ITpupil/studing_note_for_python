import smtplib
from email.mime.text import MIMEText
from email.header import Header
import base64
import pysnooper

from config import HOST,USER,LICENSE_CODE,SENDER,RECEIVERS,SENDER_INFO,SUBJECT,STYLE,creat_cve_table

class sendCveEmail(object):
    def __init__(self, cves):
        self.cves=cves
        self.server = smtplib.SMTP() 
        self.server.connect(HOST)
        self.server.login(USER,LICENSE_CODE)
        # self.send()

    def pressData(self):#组装cve信息的html表格
        td=""
        for cve in self.cves:
            td += f"<tr><td style=\"{STYLE.get('td')}\">{cve[0]}</td><td style=\"{STYLE.get('td')}\" align=\"left\">{self.outBase64(cve[1])}</td><td style=\"{STYLE.get('td')}\">{cve[2]}</td><td style=\"{STYLE.get('td')}\"><a href=\"{self.outBase64(cve[3])}\" target=\"_blank\">点击前往</a></td></tr>"
        cve_table= creat_cve_table(td)
        return cve_table

    def outBase64(self,base64_string):
        return str(base64.b64decode(base64_string),'utf-8')

    def send(self):
        message = MIMEText(self.pressData(), 'html', 'utf-8')
        message['From'] = SENDER_INFO
        message['To'] = ','.join(RECEIVERS)
        message['Subject'] = Header(SUBJECT, 'utf-8')
        self.server.sendmail(SENDER,RECEIVERS,message.as_string())
        print('邮件发送完成')



