import requests
import re
import json

def get_one_page(url):
    headers={'User-Agent':' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'}
    response=requests.get(url,headers)
    if response.status_code==200:
        return response.text
    return None

def parse_one_page(html):
    pattern=re.compile('<em.*?>(.*?)</em>.*?<span.*?"title">(.*?)</span>.*?<p.*?>(.*?)&nbsp.*?<br>(.*?)&nbsp.*?</p>',re.S)
    items=re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            'title':item[1],
            'director':item[2].strip()[3:] if len(item[2])>3 else '',
            'time':item[3].strip(),
        }
def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        # print(json.dumps(content))
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(start):
    url='https://movie.douban.com/top250?start='+str(start)+'&filter='
    html=get_one_page(url)
    result=re.search('<ol.*?>(.*?)</ol>',html,re.S) #得到网页中关于排行榜的内容
    for item in parse_one_page(result.group(1)):
        write_to_file(item)

if __name__=='__main__':
    for i in range(10):
        main(start=i*25)