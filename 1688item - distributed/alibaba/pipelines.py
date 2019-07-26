# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from urllib.parse import urlparse
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from os.path import join, basename
import csv
from .settings import filename


class AlibabaPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for i in item['image_urls']:
            # meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
            yield Request(i, meta={'kind': item['kind'], 'name': item['name']})

    def file_path(self, request, response=None, info=None):
         # 接收上面meta传递过来的图片名称

        return join(join(request.meta['kind'], request.meta['name']), basename(request.url))


class CsvPipeline(object):

    def __init__(self):
        # csv文件的位置，无须创建

        store_file = r'E:\1688 distri\{}.csv'.format(filename)
        self.file = open(store_file, 'a+', encoding='utf-8-sig', newline='')
        self.writer = csv.writer(self.file, dialect='excel')

    def process_item(self, item, spider):
        if item['name']:
            self.writer.writerow([item['kind'], item['name'], item['price'], item['link']])
        return item

    def open_spider(self, spider):
        self.writer.writerow(['关键词', '店家', '价格', '网址'])

    def close_spider(self, spider):
        self.file.close()
