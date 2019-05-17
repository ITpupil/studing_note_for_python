import requests

r =requests.get('https://python123.io/ws/demo.html') 

demo = r.text
# print(demo)


# 上行遍历  (.parent 父标签)(.parents  先辈标签)
# 下行遍历  (.contents）(.children)(.descendants)
# 平行遍历  (.next_sibling)(previous_subling)(.next_siblings)(previous_sublings

from bs4 import BeautifulSoup

soup =BeautifulSoup(demo,"html.parser")

print(soup.head)
print(soup.body.contents)
print(soup.head.children)
print(soup.head.descendants)# 儿孙节点


# 下行遍历
for child in soup.body.children:
    print(child,'soup.body.children')

for child in soup.body.descendants:
    print(child,'soup.body.descendants')

# 上行遍历
for parent in soup.a.parents:
    if parent:
        print(parent.name)
    else:
        print(parent,111111111)


# 平行遍历(.next_sibling)(previous_subling)(.next_siblings)(previous_sublings
# 平行遍历发生在同一个父标签节点下

