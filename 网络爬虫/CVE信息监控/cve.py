import requests,base64
from bs4 import BeautifulSoup
from cveMysqlPress import cveMysqlPress
from sendEmail import sendCveEmail

# 获取最新到CVE列表,返回包含cve的url列表
def getCVES():
    try:
        url = 'https://cassandra.cerias.purdue.edu/CVE_changes/today.html'
        res = requests.get(url)#, headers=headers, timeout=60)
        todayCVES = getTodayCVES(res.text, 'New entries:', 'Graduations')
        soup = BeautifulSoup(todayCVES, 'html.parser')
        cve_list=[]
        for a in soup.find_all('a'):
            cve_list.append(a['href'])
            # print(a['href'])
            # print(a.string)
        return cve_list
    except Exception as e:
        print(e)

# 获取文本中间内容
def getTodayCVES(content, startStr, endStr):
    startIndex = content.index(startStr)
    if startIndex >= 0:
        startIndex += len(startStr)
        endIndex = content.index(endStr)
    return content[startIndex:endIndex]

#将数据进行base64编码
def inBase64(data):
    return str(base64.b64encode(data.encode('utf-8')),'utf-8')

#将base64数据解码成字符串信息
def base64Out(data):
    return str(base64.b64decode(data),'utf-8')

#解析每个url的信息
def getCVEDetail(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text,'html.parser')

    cveId = soup.find(nowrap="nowrap").find('h2').string

    cveDetailUrl = inBase64(soup.find_all('a')[69]['href'])
    table = soup.find(id="GeneratedTable").find('table')
    description = inBase64(table.find_all('tr')[3].find('td').string)
    dateEntryCreated = table.find_all('tr')[10].find('td').string
    return {'cveId':cveId,
            'description':description,
            'dateEntryCreated':dateEntryCreated,
            'cveDetailUrl':cveDetailUrl}

#全流程执行脚本
def main():
    cm= cveMysqlPress() #实例化数据库脚本
    cveList = getCVES() #获取cve列表
    for cveUrl in cveList:#更新cve数据
        cm.insert_data(getCVEDetail(cveUrl))
    cves_info = cm.query_data()#读取cve数据，默认为今天,其他时间 使用YYYY-MM-DD格式
    sendCveEmail(cves_info)#发送cve信息邮件

#全流程执行脚本 + 显示进度条版
def main2():
    cm= cveMysqlPress() #实例化数据库脚本
    cveList = getCVES() #获取cve列表
    print('==========start instertting cves data============')
    for cveUrl in cveList:#更新cve数据
        percent = round(round((cveList.index(cveUrl)+1)/len(cveList),2)*100)
        str_percent = f"cves information instertting:[{percent}%]"
        print(str_percent,end='',flush=True)
        cm.insert_data(getCVEDetail(cveUrl))
        print('\b'*len(str_percent),end='')
    print('\n==========complete cves data instertting============')
    cves_info = cm.query_data()#读取cve数据，默认为今天,其他时间 使用YYYY-MM-DD格式
    sendCveEmail(cves_info)#发送cve信息邮件

#用于已经完成数据采集后 再次发送邮件
def main_only_query_data():
    cm= cveMysqlPress() #实例化数据库脚本
    cves_info = cm.query_data()#读取cve数据，默认为今天,其他时间 使用YYYY-MM-DD格式
    scm=sendCveEmail(cves_info)#实例化邮件发送脚本
    scm.send()#发送cve信息邮件


if __name__ == '__main__':
    # main2()
    main_only_query_data()
