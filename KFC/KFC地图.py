# !/user/bin/env/python 
# encoding:utf-8
# Author : mzyang
# @Date  : 2019/4/14


import pandas as pd
from pyecharts import Geo
import re

# 保存省份名称的列表
attrs = []

# 保存餐厅数目
values = []

# pandas读取存有数据的Excel文件
df = pd.read_excel(r'E:\pytotal\PY 3.7\KFC\KFC.xls')

# 选取省份的一列
provinces = dict(df['省'].value_counts())
#查看数据
print(provinces)

# 根据pyecharts里面的配置文件修改省的名称
for province in provinces.keys():
    if '省' in province:
        item = province.replace('省', '')
    elif '自治区' in province:
        item = province.replace('自治区', '')
    else:
        item = province
    attrs.append(item)

for value in provinces.values():
    values.append(value)

# 检查省份还有店数目的数据，可不写
print(attrs)
print(values)


# 创建地图
geo = Geo('我国大陆KFC省份分布热点图', '数据来自肯德基餐厅信息查询', page_title='KFC', title_color="#fff", title_pos="center", width=1280, height=720, background_color='#404a59')
geo.add('', attrs, values, visual_range=[0, 1000], type='effectScatter', visual_text_color='#fff', symbol_size=15, is_visualmap=True, is_roam=False, )

# 分析结果保存为html文件
geo.render(path=r"E:\pytotal\PY 3.7\KFC\KFC省份分布图.html")
