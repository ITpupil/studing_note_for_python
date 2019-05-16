HOST = " **************** "  #设置服务器
USER = "****************"    #用户名
LICENSE_CODE = "****************"   #授权码 

SENDER = '****************' #发送邮件的账户
RECEIVERS = ['****************@****************.com']  # 接收邮件的账户

SENDER_INFO = "CVE监控脚本" # message['From']

SUBJECT = "每日CVE信息 - 资讯快车" #邮件标题

CVE_TABLE='''
  <table border="1" style="font-family:Arial;width:100%">
    <tr>
        <th>CVE - ID</th>
        <th>Recently updated information</th>
        <th>Initial creation time</th>
        <th>Detail link</th>
    </tr>
    {}
  </table>
'''