# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import csv
from scrapy.pipelines.images import ImagesPipeline
from .settings import filename
from scrapy import Request


class DgkeyPipeline(object):

    def __init__(self):
        # csv文件的位置，无须创建

        store_file = r'E:\dgkeydata\{}.csv'.format(filename)
        self.file = open(store_file, 'a+', encoding='utf-8-sig', newline='')
        self.writer = csv.writer(self.file, dialect='excel')

    def process_item(self, item, spider):
        if item['no']:
            self.writer.writerow([item['no'], item['manufacture'], item['kind'], item['price'], item['general'], item['special'], item['piclink'],item['picpath'], item['itemlink']])
        return item

    def open_spider(self, spider):
        self.writer.writerow(['零件编号', '生产商', '种类', '价格', '一般信息', '常规', '图片链接', '图片路径', '产品链接'])

    def close_spider(self, spider):
        self.file.close()


# class PicPipeline(ImagesPipeline):
#     def get_media_requests(self, item, info):
#         for i in item['image_urls']:
#             yield Request(i, meta={'path': item['picpath']})
#
#     def file_path(self, request, response=None, info=None):
#         path = request.meta['path']
#         return path