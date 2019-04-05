# !/user/bin/env/python
# encoding:utf-8
# Author : mzyang
# @Date  : 2019/3/30


import json
import requests
import pandas as pd
from pandas import DataFrame
from lxml import etree
import re
import matplotlib.pyplot as plt
import matplotlib


# 对书本的结构比较散的属性进行整理
def get_book_info(binfo, cc):
    i = 0
    rss = {}
    k = ''
    v = ''
    f = 0
    clw = []
    for c in cc:
        if '\n' in c:
            if '\xa0' in c:
                clw.append(c)
        else:
            clw.append(c)

    for m in binfo[0]:
        if m.tag == 'span':
            mlst = m.getchildren()
            if len(mlst) == 0:
                k = m.text.replace(':', '')
                if '\xa0' in clw[i]:
                    # 需要m.tag=='a'下的值
                    f = 1
                else:
                    v = clw[i].replace('\n', '').replace(' ', '')
                i += 1
            # 下面有子span 一种判断是m.attrs == {}，不够精细
            elif len(mlst) > 0:
                for n in mlst:
                    if n.tag == 'span':
                        k = n.text.replace('\n', '').replace(' ', '')
                    elif n.tag == 'a':
                        v = n.text.replace('\n', '').replace(' ', '')

        elif m.tag == 'a':
            if f == 1:
                v = m.text.replace('\n', '').replace(' ', '')
                f = 0
        elif m.tag == 'br':
            if k == '':
                print(i, 'error')
            else:
                rss[k] = v
        else:
            print(m.tag, i)
    return rss


# 读取搜索关键字Excel数据
bsdf = pd.read_excel(r'E:\pytotal\doubanbookspider\searchlist.xlsx')
blst = list(bsdf['搜索关键字'])
l = []
n = 0
for bn in blst:
    # 添加账号cookie请求，请求太多会被豆瓣禁止
    headers = {
        'Cookie': 'bid=ISJaNETDSYc; douban-fav-remind=1; __utmz=30149280.1551799803.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); viewed="4737329"; gr_user_id=06249ddc-f0d6-4635-a1a5-a4c1bf7fb988; __utma=30149280.1079541945.1551799803.1553925321.1553928088.3; __utma=81379588.1420705545.1553928088.1553928088.1553928088.1; __utmz=81379588.1553928088.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _pk_id.100001.3ac3=664d150dc8518cba.1553925319.2.1553928088.1553925319.; _vwo_uuid_v2=D7FB1CB3F05DFA6A7008783D4CAC2310B|13ce165dae2523cbff25da847d6a72e6; dbcl2="191673215:EW1qos0/vpE"; ck=8LOa'}
    response = requests.get('https://book.douban.com/j/subject_suggest?q={0}'.format(bn), headers=headers)

    rj = json.loads(response.text)

    for i in rj:
        res = {}
        if 'subject' in i['url']:
            n += 1
            html = requests.get(i['url'], headers=headers)
            con = etree.HTML(html.text)
            for bname in con.xpath('//*[@id="wrapper"]/h1/span/text()'):
                res['搜索关键字'] = bn
                res['书名'] = bname
                res['豆瓣id'] = i['id']
            binfo = con.xpath('//*[@id="info"]')
            cc = con.xpath('//*[@id="info"]/text()')
            # 添加处理过的属性
            res.update(get_book_info(binfo, cc))

            # 获取评价及人数
            bmark = con.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')[0]
            if bmark:
                if bmark == ' ':
                    bits = con.path('//*[@id="interest_sectl"]/div/div[2]/div/div[2]/span/a/text()')
                    if bits == '评价人数不足':
                        res['评分'] = ' '
                        res['评价人数'] = '评价人数不足'
                    else:
                        res['评分'] = ' '
                        res['评价人数'] = ' '
                else:
                    res['评分'] = bmark.replace(' ', '')
                    for bhnum in con.xpath('//*[@id="interest_sectl"]/div/div[2]/div/div[2]/span/a/span/text()'):
                        res['评价人数'] = bhnum
            l.append(res)
outdf = pd.DataFrame(l)
# 数据去重
outdf.drop_duplicates(subset=['豆瓣id'], keep='first', inplace=True)
outdf.to_excel('results.xlsx', index=False)
len(set(list(outdf['出版社'])))
print('一共有{0}本书，{1}个作者，{2}个出版社；'.format(len(outdf), len(set(list(outdf['作者']))), len(set(list(outdf['出版社'])))))
# 前几位的作者
print(outdf['作者'].value_counts().head(4))
outdf = pd.read_excel(r'E:\pytotal\doubanbookspider\results.xlsx')
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_excel(r'E:\pytotal\doubanbookspider\results.xlsx')
print(df)

print('一共有{0}本书，{1}个作者，{2}个出版社；'.format(len(df), len(set(list(df['作者']))), len(set(list(df['出版社'])))))
# 查看书名
print((df['书名']), end='\n\n')
# 作者统计
print(df['作者'].value_counts(), end='\n\n')
# 查看‘冰与火之歌’的结果
print(outdf.loc[df['搜索关键字'] == '冰与火之歌', ['书名', '评分', '定价', '豆瓣id']], end='\n\n')
# 查看所有书的出版社的前5
print(df['出版社'].value_counts().head(5), end='\n\n')
# 保存出版社的图标
points = DataFrame(df['出版社'].value_counts())
points.plot(kind='bar', figsize=(10, 5))
plt.savefig(r'E:\pytotal\doubanBookSpider\results.png', bbox_inches='tight')
plt.show()

