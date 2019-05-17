
# (.prettify()方法)

import requests

r =requests.get('https://python123.io/ws/demo.html') 
demo = r.text

from bs4 import BeautifulSoup
soup =BeautifulSoup(demo,"html.parser")

print(soup.prettify())
print(soup.a.prettify())

# UTF-8编码