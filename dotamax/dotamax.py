# !/user/bin/env/python 
# encoding:utf-8
# Author : mzyang
# @Date  : 2019/7/31

import requests
import json
import csv
import time


def get_info():
    # 抓包得到的网址
    url = 'https://api.maxjia.com/api/hero/stat/v3/?&max_id=9439326&game_type=dota2&imei=7c7635a95a974919&os_type=Android&os_version=5.1.1&version=4.4.5&lang=zh-cn'

    info_url = 'https://api.maxjia.com/api/hero/detail/overview/?name={}&max_id=9439326&game_type=dota2&imei=7c7635a95a974919&os_type=Android&os_version=5.1.1&version=4.4.5&lang=zh-cn'

    # 模拟手机客户端的请求headers
    headers = {
        'Refer': 'http://api.maxjia.com/',
        'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36 ApiMaxJia/1.0',
        'Cookie': 'phone_num=0009040704010909060003;pkey=MTU2NDUwODIzNi4zMTg1NjUwODg3MTJfMWhrcGhiYnRmZWRob3FydHg__;maxid=9439326',
        'Host': 'api.maxjia.com',
        'Connection': 'close'
    }

    # 请求网址
    result = requests.get(url, headers=headers)

    l = []
    l6 = []

    # 返回的数据是json
    final = json.loads(result.text)

    for i in final['result']['stat']:
        l.append(i['img_name'])

    for a in l:
        print(a)
        d = {}

        # 获取信息
        result2 = requests.get(info_url.format(a), headers=headers)
        final2 = json.loads(result2.text)

        d['英雄'] = final2['result']['hero_info']['hero_name']

        d['关键词'] = final2['result']['hero_base_info']['key_name']

        d['胜率'] = final2['result']['hero_a_win_rate']
        d['图片链接'] = final2['result']['hero_img']
        d['本月使用人数'] = final2['result']['match_count']
        d['本月使用人数排名'] = final2['result']['match_count_rank']
        l3 = []
        for b in final2['result']['hero_items']:
            l3.append(b['item_info']['alternative_name'])
        d['热门物品'] = l3

        l4 = []
        for c in final2['result']['skill_seq']['abilities_list']:
            string = '[' + c['dname'] + ']' + '\n' + c['desc']
            l4.append(string.replace('\n', ' '))

        d['技能'] = l4

        l5 = []
        num = 1
        for e in final2['result']['special_bonus']:
            l5.append('天赋{}：'.format(num))
            num += 1
            for f in e:
                l5.append(f['desc'])
        d['天赋'] = l5
        l6.append(d)
    return l6


# 创建csv文件
def create_csv():
    file = r'E:\pytotal\dota.csv'
    with open(file, 'a+', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f, dialect='excel')
        writer.writerow(['英雄', '关键词',  '胜率', '图片链接', '本月使用人数', '本月使用人数排名', '热门物品', '技能', '天赋'])


# 数据保存
def write_csv(d):
    date = time.strftime('%m%d')
    file = r'E:\pytotal\dota_{}.csv'.format(date)
    with open(file, 'a+', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f, dialect='excel')

        writer.writerow([d['英雄'], d['关键词'], d['胜率'], d['图片链接'], d['本月使用人数'], d['本月使用人数排名'], d['热门物品'], d['技能'], d['天赋']])


def main():
    con = get_info()
    create_csv()
    for i in con:
        write_csv(i)
    print('搞定')


if __name__ == '__main__':
    main()
