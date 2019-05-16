import requests,base64
from bs4 import BeautifulSoup
from cveMysqlPress import cveMysqlPress
from sendEmail import sendCveEmail



def getCVES():# 获取最新到CVE列表
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



def getTodayCVES(content, startStr, endStr): # 获取文本中间内容
    startIndex = content.index(startStr)
    if startIndex >= 0:
        startIndex += len(startStr)
        endIndex = content.index(endStr)
    return content[startIndex:endIndex]

def inBase64(data):
    return str(base64.b64encode(data.encode('utf-8')),'utf-8')

def base64Out(data):
    return str(base64.b64decode(data),'utf-8')

import pysnooper

# @pysnooper.snoop()
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
    # x=0
    # for a in soup.find_all('a'):
    #     print(a,x)
    #     x+=1


# url = 'http://cve.mitre.org/cgi-bin/cvename.cgi?name=2012-6652'
# # getCVEDetail(url)
# cm = cveMysqlPress()
# cm.insert_data(getCVEDetail(url))

if __name__ == '__main__':
    cm= cveMysqlPress() #实例化数据库脚本

    ################不需要更新数据时注释本段代码######################
    # cveList = getCVES() #获取cve列表
    # for cveUrl in cveList:#更新cve数据
    #     cm.insert_data(getCVEDetail(cveUrl))
    #################不需要更新数据时注释本段代码######################
    
    cves_info = cm.query_data()#读取cve数据，默认为今天,其他时间 使用YYYY-MM-DD格式
    sendCveEmail(cves_info)#发送cve信息邮件
