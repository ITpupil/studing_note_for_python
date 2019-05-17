# 数据库配置
DB_HOST = 'localhost'
DB_USER = ' *** '
DB_PASSWORD = ' *** '
DATABASE = ' cves '

SQL_TABLE_CREATED = '''
create table if not exists cves(
cveId VARCHAR(20),
description VARCHAR(5000),
dateEntryCreated VARCHAR(20),
cveDetailUrl VARCHAR(100),
updatetime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)
'''

# 发送邮件脚本配置
HOST = "smtp.qq.com"  #设置服务器 
USER = "xxx@qq.com"    #用户名
LICENSE_CODE = " ***  "   #授权码 有的邮件服务器（如：某公司邮箱）没有设置，可以直接使用密码

SENDER = 'xxx@qq.com' #发送邮件的账户
RECEIVERS = ['xxx@qq.com','xxx@qq.com']  # 接收邮件的账户

SENDER_INFO = "CVE监控脚本" # message['From'] 发件人信息（或昵称）
SUBJECT = "每日CVE信息 - 资讯快车" #邮件标题

#邮件信息组装配置

STYLE = {
    'table':"border-collapse:collapse;font-family:\"Trebuchet MS\", Arial, Helvetica, sans-serif;width:100%",
    'th':"font-size:1.1em;padding-top:5px;padding-bottom:4px;background-color:#A7C942;color:#ffffff;",
    'td':"font-size:1em;border:1px solid #98bf21;padding:3px 7px 2px 7px;color:#000000;background-color:#EAF2D3;"
}

TH = f'''
<th style="{STYLE.get('th')}">CVE - ID</th>
<th style="{STYLE.get('th')}">更新信息</th>
<th style="{STYLE.get('th')}">创建时间</th>
<th style="{STYLE.get('th')}">详 情</th>
'''

def creat_cve_table(td):
    return f'''<table style="{STYLE.get('table')}"><tr>{TH}</tr>{td}</table>'''
