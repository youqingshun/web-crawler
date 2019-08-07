import requests
import re


def openurl(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    try:
        r = requests.get(url, headers = headers, timeout = 20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('无法访问网页' + url)


if __name__ == '__main__':
    douban_250 = []
    f = open('db.txt', 'w', encoding='utf-8')
    f.write('rank' + ' ' + 'name' + ' ' + 'countries' + ' ' + 'directors'+'\n')

    for i in range(10):
        url = 'https://movie.douban.com/top250?start='
        url += str(i * 25)
        text = openurl(url)
        ranks = re.findall('<em class="">(.*)</em>', text)
        movie_names = re.findall('<img width="100" alt="(.*)" src="https', text)
        counties = re.findall('&nbsp;/&nbsp;(.*)&nbsp;/&nbsp;',text)
        directors = re.findall('导演: (.*)&nbsp;&nbsp;&nbsp;主演', text)
        z = zip(ranks, movie_names, counties, directors)
        #print(directors)

        for i in z:
            douban_250.append(i)


        for i in douban_250:
            f.writelines(str(i) + '\n')

