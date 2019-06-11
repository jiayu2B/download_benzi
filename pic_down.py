#coding=utf-8
import urllib.request
import urllib.parse

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
    node1 = re.compile('''<div id="post-comic">.*</div>''')
    link = node1.findall(HTML)
    node2 = re.compile('''http.*?jpg''')
    links = node2.findall(link[0])

    return links
links = pic_down.dl("https://shikotch.net/ja/comic/31266/")
print(links)
