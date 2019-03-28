# !/user/bin/env/python 
# encoding:utf-8
# Author : mzyang
# @Date  : 2019/3/27

import requests
from bs4 import BeautifulSoup
import csv
import re
import pandas as pd
import jieba
import matplotlib.pyplot as pt
from wordcloud import WordCloud,ImageColorGenerator


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_uuid=8B14B95F-A4C5-6745-8396-AFCA29B84AFF24752infoc; CURRENT_FNVAL=16; buvid3=AF5409F4-F62C-4CCD-BF46-BE19C8A9013547155infoc; stardustvideo=1; rpdid=kxqkokspxqdossipwiiww; sid=971er1fv; DedeUserID=15998382; DedeUserID__ckMd5=71330c5d5133c166; SESSDATA=c4a17b6f%2C1556265761%2Cfa882631; bili_jct=4a7391983b065f18628c377e618ddcc5; LIVE_BUVID=AUTO7615536737645433; _dfcaptcha=44b403b8a0e274a80c664c9644f3fcf9; fts=1553673817',
    'Host': 'www.bilibili.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
}


# 获取目标视频的特定id值
def get_oid(id):
    url = 'https://www.bilibili.com/video/av{}'.format(id)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        text = response.text
        pattern = re.compile('\\"cid\\":(\\d+),')
        return re.search(pattern, text).group(1)
    else:
        print('Failed to get oid')


# 利用oid值接入api，获取弹幕内容
def get_content(id):
    url = 'https://api.bilibili.com/x/v1/dm/list.so?oid={}'.format(id)
    content = requests.get(url).content
    data = str(content, 'utf-8')
    bsObj = BeautifulSoup(data, 'lxml')
    l = []
    for comment in bsObj.select('d'):
        l.append(comment.get_text())
    return l


def save_data(l):
    df = pd.DataFrame(l)
    df.to_csv(r'E:\pytotal\bilibllcomments\result.csv', encoding='utf_8_sig')


def ana_result():
    file = r'E:\pytotal\bilibllcomments\result.csv'
    df = pd.read_csv(file, header=None)
    # 利用jieba库分词
    text = ''
    for line in df[1]:
        text += ' '.join(jieba.cut(line))
    # 生成词云
    bgi = pt.imread(r'E:\pytotal\bilibllcomments\佩奇.jpg')
    wc = WordCloud(
        background_color='white',
        mask=bgi,
        max_words=2000,
        max_font_size=80,
        random_state=30,
    )
    wc.generate_from_text(text)
    process_word = WordCloud.process_text(wc, text)
    sort = sorted(process_word.items(), key=lambda e: e[1], reverse=False)
    img_colors = ImageColorGenerator(bgi)
    wc.recolor(color_func=img_colors)
    pt.imshow(wc)
    pt.axis('off')
    wc.to_file(r'E:\pytotal\bilibllcomments\result.jpg')
    print('done')


def main():
    # 40997001为视频的av号，直接可以在网址栏处获得
    result = get_oid(40997001)
    l = get_content(result)
    save_data(l)
    ana_result()


if __name__ == '__main__':
    main()


