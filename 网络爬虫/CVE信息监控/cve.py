import requests
from bs4 import BeautifulSoup

def getCVES():# 获取最新到CVE列表
    try:
        url = 'https://cassandra.cerias.purdue.edu/CVE_changes/today.html'
        res = requests.get(url)#, headers=headers, timeout=60)
        todayCVES = getTodayCVES(res.text, 'New entries:', 'Graduations')
        soup = BeautifulSoup(todayCVES, 'html.parser')
        for a in soup.find_all('a'):
            
            print(a['href'])
            print(a.string)
    except Exception as e:
        print(e)

def getTodayCVES(content, startStr, endStr): # 获取文本中间内容
    startIndex = content.index(startStr)
    if startIndex >= 0:
        startIndex += len(startStr)
        endIndex = content.index(endStr)
    return content[startIndex:endIndex]

# getCVES()

# http://cve.mitre.org/cgi-bin/cvename.cgi?name=2012-6652
import pysnooper

@pysnooper.snoop()
def getCVEDetail(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text,'html.parser')

    cveId = soup.find(nowrap="nowrap").find('h2').string

    cveDetailUrl = soup.find_all('a')[69]['href']
    table = soup.find(id="GeneratedTable").find('table')
    description = table.find_all('tr')[3].find('td').string
    dateEntryCreated = table.find_all('tr')[10].find('td').string
    return {'cveId':cveId,
            'description':description,
            'dateEntryCreated':dateEntryCreated,
            'cveDetailUrl':cveDetailUrl}
    # x=0
    # for a in soup.find_all('a'):
    #     print(a,x)
    #     x+=1


url = 'http://cve.mitre.org/cgi-bin/cvename.cgi?name=2012-6652'
getCVEDetail(url)