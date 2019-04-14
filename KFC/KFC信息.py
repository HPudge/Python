# !/user/bin/env/python 
# encoding:utf-8
# Author : mzyang
# @Date  : 2019/4/12


import requests
from bs4 import BeautifulSoup
import re
import xlwt
import time



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
}

url = 'http://www.kfc.com.cn/kfccda/storelist/index.aspx'

res = requests.get(url, headers=headers)

# 解析网页文本
result = BeautifulSoup(res.text, 'html.parser')

r = []
# 获取站点的城市列表
citys = result.select('#container > div.wrapper > div.store_wrap > div > div.store_content > div.store_top > div > div.shen > ul')
for city in citys:
    location = city.get_text()
    # 整理数据，去除不要的省份信息
    location = re.sub('[A-Z]', ' A', location)
    location = re.sub('[A-Z].*? ', '', location)
    # 城市列表
    c = location.split()
    for i in c:
        r.append(c)

l = []


def get_detail(page, cname):
    final_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    data = {
        'cname': cname,
        'pid': '',
        'pageIndex': page,
        'pageSize': '10',
    }
    # ajax请求
    response = requests.post(final_url, data=data)
    # 判断是否获取空列表
    if not bool(response.json().get('Table1')):
        pass
    else:
        ori = response.json()['Table1']
        # 删除列表中不要的信息并保存进列表
        for a in ori:
            a.pop('rownum')
            l.append(a)
            print(l)
    return response.json()['Table1']


# 保存Excel文件
def save_data(li):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('kfc_info', cell_overwrite_ok=True)

    worksheet.write(0, 0, '省')
    worksheet.write(0, 1, '市')
    worksheet.write(0, 2, '店名')
    worksheet.write(0, 3, '地址')
    worksheet.write(0, 4, '特色')

    for n in range(len(l)):
        worksheet.write(n + 1, 0, li[n]['provinceName'])
        worksheet.write(n + 1, 1, li[n]['cityName'])
        worksheet.write(n + 1, 2, li[n]['storeName'])
        worksheet.write(n + 1, 3, li[n]['addressDetail'])
        worksheet.write(n + 1, 4, li[n]['pro'])

    workbook.save(r'C:\Users\MZY\Desktop\kfc.xls')


def main():
    start = time.time()
    # 遍历城市列表
    for loc in c:
        # 限制速度
        time.sleep(1)
        page = 1
        while True:
            print(page)
            req = get_detail(page, loc)
            page += 1
            # 店面信息为空时 break
            if not bool(req):
                print('done!')
                break

    save_data(l)
    print('保存完毕' + '共有' + str(len(l)) + '个店面信息' )
    end = time.time()
    print('用时' + str(start-end) + '秒')


if __name__ == '__main__':
    main()




