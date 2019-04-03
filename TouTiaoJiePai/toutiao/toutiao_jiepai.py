# !/user/bin/env/python
# encoding:utf-8
# Author : mzyang
# @Date  : 2019/3/1

import os
import requests
from urllib.parse import urlencode
from hashlib import md5
from multiprocessing.pool import Pool

from config import *
import pymongo

client =pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


GROUP_START = 1
GROUP_END = 5

# 请求网页
def get_page(offset):
    params = {
        'aid': '24',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc':  '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        print('请求页面出错!')



def get_images(json):
    data = json.get('data')
    if data:
        for item in data:
            image_list = item.get('image_list')
            title = item.get('title')
            for image in image_list:
                yield {
                    'image': image.get('url'),
                    'title': title
                }
# 将图片链接保存到mongoDB
def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('储存到MongoDB成功')
        return True
    return False

# 修改URL获取清晰图片的下载链接，按目录下载图片
def save_image(item):
    if not os.path.exists(r'D:\头条街拍' + os.sep + item.get('title')):
        os.mkdir(r'D:\头条街拍' + os.sep + item.get('title'))
    try:
        local_image_url = item.get('image')
        new_image_url = local_image_url.replace('list','large')
        print(new_image_url)
        response = requests.get('http:' + new_image_url)
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(r'D:\头条街拍' + os.sep + item.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb')as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to save image')


def main(offset):
    json = get_page(offset)

    for item in get_images(json):
        if item:
            print(item)
            save_image(item)
            save_to_mongo(item)
        print('no more pic')


# 线程加快效率
if __name__ == '__main__':
    pool = Pool(processes=8)
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()