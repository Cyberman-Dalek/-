#-*-encoding:utf-8-*-,
import requests
from bs4 import BeautifulSoup

f = open('状态.txt')
f.close()
for i in range(13):
    headers = {
        'HOST': '3g.renren.com',
        'User-Agent': '',
    }
    r = requests.get(
        'curpage=' + str(i) + '',
        headers)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div', class_='list')[0]
    for item in div_list.find_all('div'):
        f = open('状态.txt', 'a', encoding='gbk',errors='ignore')
        if('转自' not in item.contents[2]):
            f.write(item.contents[2])
        f.close()




