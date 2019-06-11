#coding=utf-8
import urllib.request
import urllib.parse
import os
import requests
import time
def getHtml(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=headers)  # 这里要注意，必须使用url=url，headers=headers的格式，否则回报错，无法连接字符

    page = urllib.request.urlopen(req)
    html = page.read().decode("utf-8")
    return html




import re
def dl(URL = "https://shikotch.net/ja/comic/31266/"):
    HTML = getHtml(URL)
    node0 = re.compile('''<title>.*?:''')
    Title = node0.findall(HTML)
    Title = Title[0][7:-1]
    node1 = re.compile('''<div id="post-comic">.*</div>''')
    link = node1.findall(HTML)
    print(Title)
    node2 = re.compile('''http.*?jpg''')
    links = node2.findall(link[0])

    return links, Title


links,Title= dl("https://shikotch.net/ja/comic/16014/")
print(links)


def request_download():


    root = 'D:/excited/'+Title
    print(root)

    try:
        os.makedirs(root)
    except FileExistsError as e:
        print(e)

    print("root creating success")


    for i in range(0, len(links)):
        r = requests.get(links[i])
        with open(root[:-1]+'/'+str(i)+'.jpg', 'wb') as f:
            f.write(r.content)
        print(str(i) + ' downloaded success')


request_download()
