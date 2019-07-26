# -*- coding: utf-8 -*-
from scrapy import Request, Spider
import re
from bs4 import BeautifulSoup
import requests
import time
import os
import numpy
from ..items import DgkeyItem
from scrapy_redis.spiders import RedisCrawlSpider


class DgSpider(RedisCrawlSpider):
    headpath = 'E:/dgkeydata'

    name = 'de'
    # 分布式的起始
    redis_key = 'de:start_urls'
    allowed_domains = ['digikey.cn']
    # start_urls = ['lpush de:start_urls https://www.digikey.cn/products/zh/sensors-transducers/irda-transceiver-modules/538']
    num = 0

    def parse(self, response):
    #     # 获取细分类页面
    #     links = response.xpath('//a[@class="catfilterlink"]/@href').extract()
    #     for i in links:
    #         link = 'https://www.digikey.cn' + i
    #
    #         yield Request(link, callback=self.getpage)
    #
    # def getpage(self, response):
        if response.xpath('//div[@style="padding-bottom: 5px"]/text()'):
            pages = response.xpath('//div[@style="padding-bottom: 5px"]/text()').extract()[0].strip()
            pattern = re.compile('.*?/(\d*)')
            page = int(re.findall(pattern, pages)[0])
        else:
            page = 2

        for i in range(1, page + 1):
            url = response.url + '?pageNumber={}'.format(i)
            yield Request(url, callback=self.itempage)

    def itempage(self, response):
        pages = response.xpath('//a[@id="digikeyPartNumberLnk"]/@href').extract()
        for page in pages:
            result = 'https://www.digikey.cn' + page
            print('准备访问商品页面' + result)
            yield Request(result, callback=self.get_detailpage)

    def get_detailpage(self, response):
        item = DgkeyItem()
        self.num += 1
        print(self.num)
        print(response.url)


        # 制作商零件编号
        if response.xpath('//h1[@class="seohtag"]/text()').extract():
            no = response.xpath('//h1[@class="seohtag"]/text()').extract()[0].replace('/', ' ')
            item['no'] = no

            # 类别
            kinds = response.xpath('//h2[@class="seohtag"]/a/text()').extract()
            kind = ' > '.join(kinds[1:])

            item['kind'] = kind

            # 制作商
            manufacture = response.xpath('//span[@itemprop="name"]/text()').extract()[0].replace('/', ' ')

            item['manufacture'] = manufacture

            # 价格
            priceform = response.xpath('//td[@class="catalog-pricing"]').extract_first().strip()

            a = priceform.replace('\t', '')

            soup = BeautifulSoup(a, 'lxml')
            trs = soup.find_all('tr')
            l5 = []
            for tr in trs:
                ui = []
                for td in tr:
                    ui.append(td.string.replace('\n', ''))
                result = ' '.join(ui)
                l5.append(result)
            price = numpy.array(l5).reshape(len(l5), 1)

            item['price'] = price

            # 一般属性
            general0 = response.xpath('//table[@id="GeneralInformationTable"]').extract()[0]

            a = general0.replace('\t', ' ').replace('<br>', '').replace('\n', ' ')
            del1 = re.compile(r'</*span.*?>|</*a.*?>|</*img.*?>')
            result = re.sub(del1, '', a)

            l1 = []
            l2 = []
            pattern1 = re.compile('<th .*?>(.*?)<.*?/th>', re.S)
            results1 = re.findall(pattern1, result)
            for a in results1:
                l1.append(a.strip())

            pattern2 = re.compile('<td>(.*?)</td>', re.S)
            results2 = re.findall(pattern2, result)
            for b in results2:
                l2.append(b.strip())

            general = dict(zip(l1, l2))

            item['general'] = general

            # 特殊属性
            special0 = response.xpath('//table[@id="SpecificationTable"]').extract()[0]
            c = special0.replace('\t', ' ').replace('<br>', '')
            res = re.sub(del1, '', c)

            l3 = []
            l4 = []

            res1 = re.findall(pattern1, res)
            for m in res1:
                l3.append(m.strip())

            res2 = re.findall(pattern2, res)
            for n in res2:
                l4.append(n.strip())

            special = dict(zip(l3, l4))

            item['special'] = special

            # 图片链接
            firstpic = response.xpath('//td[@class ="image-table"]/div//img/@src').extract()[0]
            if 'pna-zh-cn.jpg' not in firstpic:
                piclink = 'https:' + firstpic
            else:
                piclink = ''

            item['piclink'] = piclink



            item['itemlink'] = response.url

            # 下载图片
            header = {
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                        'upgrade-insecure-requests': '1',
                        'cookie': 'i10c.uid=1560320222822:2140; _ga=GA1.2.102241263.1560320234; EG-U-ID=E5d757aee7-e572-4ccc-a7a9-52b396473e33; _gid=GA1.2.1284065162.1561347516; WC_PERSISTENT=2qR%2fcTj0QTNq1A7kLdTsgQ4w8ag%3d%0a%3b2019%2d06%2d23+22%3a54%3a11%2e602%5f1560559417090%2d263739%5f10001%5f7170901%2c%2d7%2cCNY%5f10001; sid=180144000318897030xKJI9ABWQRNM60A47LK2V4IOSVZVN2A3SIT1MLPFHZG3TPSBJYY2IBZ7LG4ZDKJPM; SC_ANALYTICS_GLOBAL_COOKIE=77690e030271486d8ab64760dff7de83|True; rvps=7442788<SEP>7833615<SEP>1013488<SEP>7833614<SEP>2267693<SEP>3947014<SEP>3178679<SEP>9763054<SEP>6633115<SEP>8724687<SEP>8064943<SEP>9508952; WC_SESSION_ESTABLISHED=true; WC_AUTHENTICATION_7170901=7170901%2cSS4Zp0LrsM2u1mO%2fhYiDQzhylPY%3d; WC_ACTIVEPOINTER=%2d7%2c10001; WC_USERACTIVITY_7170901=7170901%2c10001%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2c7PUG5ZgxQrqwAtbYSL0PbqBNnH1eKH%2fpYz%2ftkaDxco0DxoFSZiQ9xtHMIhjIbzmLPxlnwmONcpKK%0afIKihafAw%2fDokX9lHeaz5M5WY4xrMtEZfd%2bzn9YJHs7CkfUgmDFUfqKgb22t8QRkfs5t9k1GZQ%3d%3d; i10c.ss=1561449146553; TS01b442d5=01460246b6ed41fbe219ed9384cd8c851c7b2ccabafe8a832296e3cc51c7c33249da174b5716d90e6c3d07bd927681e50245e26d22; JSESSIONID=0002AeYexwWn5UllNZy4yqdhehL:D2EFJN7PR; utag_main=v_id:016b4a5544dc009d28a97567838003072005f06a00bd0$_sn:16$_ss:0$_st:1561451556638$ses_id:1561447057849%3Bexp-session$_pn:13%3Bexp-session; i10c.uservisit=272'
                    }


            proxytext = requests.get('http://192.168.0.155:5010/get/').text
            proxy = 'http://' + proxytext

            proxies = {"http": proxy}
            path = self.headpath + '/' + time.strftime('%m%d')
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                pass

            if piclink:
                con = requests.get(piclink, headers=header, proxies=proxies)
                picpath = path + '/' + manufacture + '-' + no + '.jpg'
                item['picpath'] = picpath
                with open(picpath, 'wb') as p:
                    p.write(con.content)
            else:
                item['picpath'] = ''

            yield item

        else:
            print("---代理出错，ag----")
            yield Request(response.url, callback=self.get_detailpage)