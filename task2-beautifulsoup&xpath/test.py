import requests
from bs4 import BeautifulSoup
#from lxml import etree
from html import etree
'''
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
url='https://www.baidu.com'
html = requests.get(url, headers=headers)
html.encoding = 'UTF-8'
soup = BeautifulSoup(html.text, 'lxml')   #以上是从网络上获取html
#soup=BeautifulSoup(open('index.html', encoding='utf-8'))  # 读取本地的html，加个open函数即可
#print(soup.prettify())     # 用标准html 显示方法打印html

print(type(soup.select('title')))
print(soup.select('title')[0].get_text())
for title in soup.select('title'):
    print(title.get_text())
'''

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
url='https://www.baidu.com'
html = requests.get(url, headers=headers)
html = etree.parse(html.text)

#soup=BeautifulSoup(open('index.html', encoding='utf-8'))  # 读取本地的html，加个open函数即可

result = etree.tostring(html, pretty_print=True)#result存储网站代码
print(result)