# -*- coding: utf-8 -*-

# Scrapy settings for alibaba project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'alibaba'

SPIDER_MODULES = ['alibaba.spiders']
NEWSPIDER_MODULE = 'alibaba.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'alibaba (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    # ':authority': 'detail.1688.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'cookie':'__wapcsf__=1; UM_distinctid=16ab45844341c4-0fec122fb-d373363-1fa400-16ab4584435640; cna=FyBhFaKBBz4CAXQYmJCBMTJ7; ali_ab=113.87.195.114.1557804029879.6; ali_beacon_id=113.87.195.114.1557804977280.940660.6; lid=%E6%AF%9B%E7%AB%B9%E6%9D%A8; ali_apache_track=c_mid=b2b-27667664330cef5|c_lid=%E6%AF%9B%E7%AB%B9%E6%9D%A8|c_ms=1; CNZZDATA1261052687=1102046157-1559634805-https%253A%252F%252Fdetail.1688.com%252F%7C1559634805; h_keys="%u6df1%u5733%u8003%u52e4%u673a#%u9632%u7206%u6bef%u7ecf%u9500%u5546#%u9632%u7206%u6bef#%u5237%u5361%u95e8%u7981#LED%u9a71%u52a8#%u7535%u5b50%u5143%u4ef6%u4ef7%u683c%u67e5%u8be2#LED#%u4e07%u7528%u8868#%u5206%u6d41%u5668"; ad_prefer="2019/07/11 09:24:59"; __wapcsf__=1; cookie2=14d854764eebfab66f84032800e87430; t=55c3b8aa7711d2b7480175836533c0b3; _tb_token_=e15485aaaeb67; __cn_logon_id__=%E6%AF%9B%E7%AB%B9%E6%9D%A8; __last_loginid__=%E6%AF%9B%E7%AB%B9%E6%9D%A8; __cn_logon__=true; ali_apache_tracktmp=c_w_signed=Y; alicnweb=homeIdttS%3D96570742467609737555864229699408797724%7Ctouch_tb_at%3D1562894225366%7ChomeIdttSAction%3Dtrue%7Clastlogonid%3D%25E6%25AF%259B%25E7%25AB%25B9%25E6%259D%25A8; CNZZDATA1253659577=1891225186-1557801351-https%253A%252F%252Fshow.1688.com%252F%7C1562892188; cookie1=VWwx4MfWNa1Xn9Ra%2FNIJMjGJQpr9b8GsKKM1Zv%2BzC%2Bc%3D; cookie17=UU8Od9e0W7yEGA%3D%3D; sg=%E6%9D%A83b; csg=e02ae839; unb=2766766433; _nk_=%5Cu6BDB%5Cu7AF9%5Cu6768; last_mid=b2b-27667664330cef5; _csrf_token=1562895864558; _is_show_loginId_change_block_=b2b-27667664330cef5_false; _show_force_unbind_div_=b2b-27667664330cef5_false; _show_sys_unbind_div_=b2b-27667664330cef5_false; _show_user_unbind_div_=b2b-27667664330cef5_false; __rn_alert__=false; l=cBTBo_W7vVnV-i1kKOCN5uI8aD_TQIRAguPRwNq2i_5dzOL34BbOk0A4rHp6cjWdOjYB4k5AU999-etoi-sZ2i-l0GdC.; isg=BHZ2ikJkN-bZscL_I4h4RNqNx6y4P7pKHzVrT-BfedngIxa9SCa04S4RP7_qi7Lp'
}

DOWNLOAD_TIMEOUT = 10

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   'alibaba.middlewares.AlibabaSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'alibaba.middlewares.RandomUAMiddleware': 543,
    'alibaba.middlewares.ProxyMiddleware': 500,

}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'alibaba.pipelines.AlibabaPipeline': 1,
   'alibaba.pipelines.CsvPipeline': 200,

}
IMAGES_STORE = r'E:\1688 distri\image'
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
FEED_EXPORT_ENCODING = 'UTF-8-SIG'


# the default user_agent_list composes chrome,I E,firefox,Mozilla,opera,netscape
user_agent_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

filename = input('输入 csv 名字： ')


SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 确保所有的爬虫通过 Redis 去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 调度持久化，不清理 Redis 缓存，允许暂停/启动爬虫
SCHEDULER_PERSIST = True

# 主机地址，主机的话可以注释
# REDIS_URL = 'redis://root@192.168.0.155:6379'
