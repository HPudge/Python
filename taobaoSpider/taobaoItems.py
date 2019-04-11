import requests
import re
import json
import xlwt
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
from pandas import DataFrame

# 令pyplot生成的图中的中文和负号能正确显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False

# requests的请求头
headers = {
    'cookie': 'thw=cn; cna=wgvwFIi+sywCAduILPDULC87; t=6ae4130dc7b32ee9476d3f7657bcdd3f; uc3=vt3=F8dByEiTlj5SZWS7dco%3D&id2=UU8Od9e0W7yEGA%3D%3D&nk2=oBGcpGdc&lg2=VFC%2FuZ9ayeYq2g%3D%3D; tracknick=%5Cu6BDB%5Cu7AF9%5Cu6768; lgc=%5Cu6BDB%5Cu7AF9%5Cu6768; _cc_=VT5L2FSpdA%3D%3D; tg=0; enc=T4mW0LaMA9RU%2FQWhnDTgSCrGmRW7eQJOmNJrdbN%2BWAkYvcPKSU3opCZYgVQp1z%2BfYDNL7I1eIdZ7hLHHNTaZXQ%3D%3D; mt=ci=3_1; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; UM_distinctid=16a003e7c77583-07a84d14468ac-9333061-e1000-16a003e7c787ff; _m_h5_tk=85b01caf62d645fec7293ece7432f65f_1554801767223; _m_h5_tk_enc=fb3cd93a86d2ab9f184357042d3815fd; cookie2=12d39749a9fb578cace017d7963cee68; _tb_token_=e533be78ebe7b; v=0; swfstore=45886; _uab_collina=155482315403381190240602; uc1=cookie14=UoTZ4Mc%2FxXn0yA%3D%3D; x5sec=7b227365617263686170703b32223a223766623938323861613036303865623731376364333436303338303830313139434b4f59732b5546454f5362346633773363755950786f4d4d6a63324e6a63324e6a517a4d7a7379227d; JSESSIONID=42F63D983CA3B403F3739DC7619CA24F; l=bBOktVvgvnxDJpWQBOCwCuI8LC7TjIRAguPRwCjXi_5Cl6Ls2a_OlMEAXFp6Vj5RsvYB4-L8Y1J9-etki; isg=BIWF8Z47dag_g1HfTzQzHOcMlMF_6ji7rlJQQYfqTbzLHqWQT5KGpG78LAJNXlGM',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

DATA =[]
# 对比不同页数的淘宝页面得到的网页规律，实现翻页
# 后面的淘宝物品基本不会看到，所以选择前50页的物品
for i in range(1, 51):
    bcoffset = 9 - i * 3
    ntoffset = 12 - i * 3
    s = 44 * (i - 1)
    url = 'https://s.taobao.com/search?q=python&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180430&ie=utf8&bcoffset={0}&ntoffset={1}&p4ppushleft=1%2C48&s={2}'.format(bcoffset, ntoffset, s)
    print(url)
    response = requests.get(url, headers=headers)
    html = response.text
    # 打印html可以得知html是json格式的数据
    content = re.findall(r'g_page_config = (.*?) g_srp_loadCss', html, re.S)[0].strip()[:-1]
    # 格式化数据
    content = json.loads(content)
    # 获取信息列表
    data_list = content['mods']['itemlist']['data']['auctions']
    # 提取数据
    for item in data_list:
        # 物品的名称有html标签，删去
        title = item['title'].translate(str.maketrans('', '', '<span class=H>python</span>'))
        # 有些物品的详情页地址不完整，补全
        if 'https:' not in str(item['detail_url']):
            detail = 'https:' + str(item['detail_url'])
        else:
            detail = str(item['detail_url'])
        temp = {
            '名称': title,
            '价格': item['view_price'],
            '付款人数': item['view_sales'],
            '包邮': '否' if float(item['view_fee']) else '是',
            '天猫': '是' if item['shopcard']['isTmall'] else '否',
            '地区': item['item_loc'],
            '店名': item['nick'],
            '详情页': detail,
        }
        if temp not in DATA:
            DATA.append(temp)

print('一共爬取到' + str(len(DATA)) + '个物品。')

# 数据保存为Excel
f = xlwt.Workbook(encoding='utf-8')
sheet01 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)

sheet01.write(0, 0, '名称')
sheet01.write(0, 1, '付款人数')
sheet01.write(0, 2, '价格')
sheet01.write(0, 3, '包邮')
sheet01.write(0, 4, '天猫')
sheet01.write(0, 5, '地区')
sheet01.write(0, 6, '店名')
sheet01.write(0, 7, '详情页')

for i in range(len(DATA)):
    sheet01.write(i + 1, 0, DATA[i]['名称'])
    sheet01.write(i + 1, 1, DATA[i]['付款人数'])
    sheet01.write(i + 1, 2, DATA[i]['价格'])
    sheet01.write(i + 1, 3, DATA[i]['包邮'])
    sheet01.write(i + 1, 4, DATA[i]['天猫'])
    sheet01.write(i + 1, 5, DATA[i]['地区'])
    sheet01.write(i + 1, 6, DATA[i]['店名'])
    sheet01.write(i + 1, 7, DATA[i]['详情页'])

f.save('results.xls')

r = pd.read_excel(r'E:\pytotal\results.xls')
# 查看爬取的数据中最多物品的网店前20名
store = DataFrame(r['店名'].value_counts().head(20))
print(store)
# 生成图片
store.plot(kind='bar', figsize=(19.20, 12.80))
plt.savefig(r'E:\pytotal\前20店.png', bbox_inches='tight')
plt.show()





