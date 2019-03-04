# !/user/bin/env/python
# encoding:utf-8
# Author : mzyang
# @Date  : 2019/2/26


import requests
from requests.exceptions import RequestException
import re
import json
from multiprocessing import Pool

# 请求网页数据
def get_page(url):
# 排除常见错误
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

# 根据目标内容制定正则表达式筛选
def parse_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield{
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:],
            'releasetime':item[4][5:],
            'comment':item[5] + item[6]
        }

# 保存数据
def save_file(content):
    with open('top100.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False) + '\n')

# 遍历榜单的全部网页
def main(offset):
    url='https://maoyan.com/board/4?offset=' + str(offset)

    html=get_page(url)

    for item in parse_page(html):
        save_file(item)
        print(item)



# 多进程加快抓取，仅为尝试
if __name__ =='__main__':
    for i in range(10):
        main(i * 10)
        pool = Pool()
        pool.map(main, [i * 10 for i in range(10)])

