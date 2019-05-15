HOST = "smtp.qq.com"  #设置服务器
USER = "xxx@qq.com"    #用户名
LICENSE_CODE = "***************"   #授权码 

SENDER = 'xxx@qq.com' #发送邮件的账户
RECEIVERS = ['xxx@qq.com','xxx2@qq.com']  # 接收邮件的账户

SENDER_INFO = "CVE监控脚本" # message['From']

SUBJECT = "每日CVE信息 - 资讯快车" #邮件标题

CVE_HTML='''
<html>
 <head>
  <meta charset="utf-8"/>
  <style>
   #customers
{
    font-family:"Trebuchet MS", Arial, Helvetica, sans-serif;
    width:100%;
    border-collapse:collapse;
}
#customers td, #customers th
{
    font-size:1em;
    border:1px solid #98bf21;
    padding:3px 7px 2px 7px;
}
#customers th
{
    font-size:1.1em;
    text-align:left;
    padding-top:5px;
    padding-bottom:4px;
    background-color:#A7C942;
    color:#ffffff;
}
#customers tr.alt td
{
    color:#000000;
    background-color:#EAF2D3;
}
  </style>
 </head>
 <body>
  <table id="customers">
    <tr>
        <th>CVE - ID</th>
        <th>最近更新信息</th>
        <th>最初创建时间</th>
        <th>详情链接</th>
    </tr>
    {}
  </table>
 </body>
</html>
'''