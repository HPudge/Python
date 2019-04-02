# !/user/bin/env/python 
# encoding:utf-8
# Author : mzyang
# @Date  : 2019/3/2

import requests
from urllib.parse import urlencode
from requests.exceptions import ConnectionError
from pyquery import PyQuery as pq
import pymongo
from lxml.etree import XMLSyntaxError
from config import *

client=pymongo.MongoClient('localhost')
db = client[MONGO_BD]

basic_url = 'https://weixin.sogou.com/weixin?'
headers={'Cookie': '',#用微信登陆一次后复制请求的cookies粘贴
         'Host': 'weixin.sogou.com',
         'Upgrade - Insecure - Requests': '1',
         'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 72.0.3626.81Safari / 537.36'
}



proxy = []
proxy_pool_url = PROXY_POOL_URL
max_count= MAX_COUNT

# 利用代理池获取代理地址
def get_proxy():
    try:
        response = requests.get(proxy_pool_url)
        if response.status_code ==200:
           return response.text
        return None
    except ConnectionError:
        print('can\'t get proxy')



def get_html(url,count=1):
    print('Crawling',url)
    print('Trying count',count)
    global proxy
    # 设置条件，防止死循环
    if count > max_count:
        print('Tried to many times.')
        return None

    try:
        # 使用代理ip请求网页
        if proxy:
            proxies={
                'http':'http://'+ proxy
            }
            response = requests.get(url,allow_redirects=False,headers=headers,proxies =proxies)
        else:
            # 获取不了代理ip就用本机ip
            response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            #搜狗的反爬虫策略是禁ip，出现了可以选择换ip继续请求
            count += 1
            print('302,antispider!!!')
            proxy = get_proxy()
            if proxy:
                # 这个代理池是免费的，因此需要多次请求
                print('Using proxy', proxy)
                return get_html(url)
            else:
                print('Get proxy Failed')
                return None

    except ConnectionError as e :
        print('Error',e.args)
        proxy = get_proxy()
        count += 1
        return get_html(url,count)


# 设置请求url
def get_index(keyword,page):
    data={
        'query': keyword,
        'type': 2,
        'page': page
    }
    queries =urlencode(data)
    url = basic_url + queries
    html = get_html(url)

# pyquery解析目标url，获取微信内容的链接
def parse_index(html):
    doc = pq(html)
    items = doc('.news-box .news-list .txt-box h3 a').items()
    for item in items:
        yield item.attr('href')

# 请求微信内容的链接，并获取网页文本
def get_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200 :
            return response.text
        return None
    except ConnectionError:
        return None

# 解析网页文本，获取信息
def parse_detail(html):
    try:
        doc = pq(html)
        title = doc('.rich_media_title').text()
        content = doc('.rich_media_content').text()
        date = doc('#post-date').text()
        nickname = doc('#js_profile_qrcode > div > strong').text()
        wechat = doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
        return {
            'title': title,
            'content': content,
            'date': date,
            'nickname': nickname,
            'wechat': wechat
        }
    except XMLSyntaxError:
        return None


def save_to_mongo(data):
    # 信息去重
    if db['wechat'].update({'title':data['title']},{'$set':data},True):
        print('Saved to Mongo',data['title'])
    else:
        print('Saved wo Mongo failed',data['title'])



def main():
    # 搜狗结果只有100页
    for page in range(1,101):
        html = get_index(KEYWORD,page)
        if html:
            articles_url = parse_index(html)
            for article_url in articles_url:
                article_html = get_detail(article_url)
                if article_html:
                    article_data=parse_detail(article_html)
                    if article_data:
                              save_to_mongo(article_data)






if __name__ =='__main__':
    main()
