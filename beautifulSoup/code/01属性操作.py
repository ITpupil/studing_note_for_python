import requests

r =requests.get('https://python123.io/ws/demo.html') 

demo = r.text
# print(demo)


from bs4 import BeautifulSoup

soup =BeautifulSoup(demo,"html.parser")

# print(soup.prettify())
# 标签获取
print(soup.title,'获取title标签')
print(soup.a,'获取a标签 只能获得第一个标签的内容')
print(soup.body,'获取body标签')

# 标签名字 name (结果是字符串)
print(soup.a.name,'标签名字 .name')
print(soup.a.parent.name,'标签父的名字 name (可以多个parent)')
print(soup.a.parent.parent.name,'标签父的名字 name (可以多个parent)')

# 标签属性 attributes--字典 使用：attrs
tag = soup.a
print(tag.attrs,'标签属性 attrs 结果是字典')
print(tag.attrs['href'],'标签属性获取，同字典操作')

# 标签里的信息(用string)  即两个尖括号中的信息<>。。。<> NavigableString
print(tag.string,'标签信息获取 string')
print(soup.p.string,'标签P的信息，信息不包含标签 string')

# 注释标签
newsoup = BeautifulSoup('<b><!--sakjdkjkljldasjkdjlajlsd --></b><p class="title"><b>这里有个注释标签</b></p>','html.parser')
print(newsoup.b.string,'会打印出注释信息 他的类型是comment类型和标签的类型不同')

