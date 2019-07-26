# -*- coding: utf-8 -*-
from scrapy import Spider, Request
import re
import requests
from urllib.parse import unquote
import os
from ..items import AlibabaItem
from scrapy_redis.spiders import RedisCrawlSpider


class BbSpider(RedisCrawlSpider):
    name = 'bb'

    redis_key = 'item:start_urls'
    filename = r'E:\1688 distri\image'

    headers = {
        ':authority': 'detail.1688.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'cookie': '__wapcsf__=1; UM_distinctid=16ab45844341c4-0fec122fb-d373363-1fa400-16ab4584435640; cna=FyBhFaKBBz4CAXQYmJCBMTJ7; ali_ab=113.87.195.114.1557804029879.6; ali_beacon_id=113.87.195.114.1557804977280.940660.6; lid=%E6%AF%9B%E7%AB%B9%E6%9D%A8; ali_apache_track=c_mid=b2b-27667664330cef5|c_lid=%E6%AF%9B%E7%AB%B9%E6%9D%A8|c_ms=1; CNZZDATA1261052687=1102046157-1559634805-https%253A%252F%252Fdetail.1688.com%252F%7C1559634805; h_keys="%u6df1%u5733%u8003%u52e4%u673a#%u9632%u7206%u6bef%u7ecf%u9500%u5546#%u9632%u7206%u6bef#%u5237%u5361%u95e8%u7981#LED%u9a71%u52a8#%u7535%u5b50%u5143%u4ef6%u4ef7%u683c%u67e5%u8be2#LED#%u4e07%u7528%u8868#%u5206%u6d41%u5668"; ad_prefer="2019/07/11 09:24:59"; __last_loginid__=%E6%AF%9B%E7%AB%B9%E6%9D%A8; CNZZDATA1253659577=1891225186-1557801351-https%253A%252F%252Fshow.1688.com%252F%7C1563153690; __wapcsf__=1; unb=2766766433; cookie2=13b91b470176165197c0dded8eac41a3; t=55c3b8aa7711d2b7480175836533c0b3; _tb_token_=e5459e3d5e967; cookie1=VWwx4MfWNa1Xn9Ra%2FNIJMjGJQpr9b8GsKKM1Zv%2BzC%2Bc%3D; cookie17=UU8Od9e0W7yEGA%3D%3D; sg=%E6%9D%A83b; csg=efa3c121; __cn_logon__=true; __cn_logon_id__=%E6%AF%9B%E7%AB%B9%E6%9D%A8; ali_apache_tracktmp=c_w_signed=Y; _nk_=%5Cu6BDB%5Cu7AF9%5Cu6768; last_mid=b2b-27667664330cef5; _csrf_token=1563154381867; _is_show_loginId_change_block_=b2b-27667664330cef5_false; _show_force_unbind_div_=b2b-27667664330cef5_false; _show_sys_unbind_div_=b2b-27667664330cef5_false; _show_user_unbind_div_=b2b-27667664330cef5_false; __rn_alert__=false; alicnweb=homeIdttS%3D96570742467609737555864229699408797724%7Ctouch_tb_at%3D1563154383066%7ChomeIdttSAction%3Dtrue%7Clastlogonid%3D%25E6%25AF%259B%25E7%25AB%25B9%25E6%259D%25A8; l=cBTBo_W7vVnV-1i9BOCNquI8aD_TdIRAguPRwNq2i_5dzTT_eJQOkcYv8n96cjWd9sYB4k5AU9w9-etuixsZ2i-l0GdC.; isg=BGVlSa19VE8IdbFi5L17weUwdCFfChmvcLh48mdKCxyrfoXwL_JZBP2cCKKt_jHs'
    }

    def parse(self, response):
        # 前10个
        targets = response.xpath('//a[@t-click-item="title"]/@href').extract()[:10]
        for i in targets:

            item = AlibabaItem()
            kind = re.findall('keywords=(.*)', response.url)[0]
            item['kind'] = unquote(kind, encoding='gbk')
            yield Request(i, headers=self.headers, callback=self.detail, dont_filter=True, meta={'data': item})

    def detail(self, response):
        print('====请求网址====  ', response.url)
        l = []
        item = response.meta['data']
        if response.xpath('//div[@id="mod-detail-title"]/h1/text()').extract():


            print('获取成功')
            item['link'] = response.url
            name = response.xpath('//div[@id="mod-detail-title"]/h1/text()').extract()[0]
            item['name'] = name.replace('/', ' ').replace('\\', ' ').replace('?', ' ').replace(':', ' ').replace('<', ' ').replace('>', ' ').replace('|', ' ').replace('"', ' ').replace('*', ' ')
            if response.xpath('//span[contains(@class,"value price-length")]/text()').extract():
                price = response.xpath('//span[contains(@class,"value price-length")]/text()').extract()[0]
                item['price'] = price
            elif response.xpath('(//div[@class="price-original-sku"]/span[@class="value"])[1]/text()').extract():
                item['price'] = response.xpath('(//div[@class="price-original-sku"]/span[@class="value"])[1]/text()').extract()[0]
            else:
                item['price'] = ' '

            # 图片路径
            # item['picpath'] = self.filename + '\\' + item['kind'] + '\\' + item['name']
            # pics = response.xpath('//img[contains(@src,"60x60")]/@src').extract()
            # for pic in pics:
            #     l.append(pic.replace('60x60', '400x400'))
            # item['image_urls'] = l
            yield item
        else:
            yield Request(response.url, headers=self.headers, callback=self.detail, dont_filter=True, meta={'data': item})
