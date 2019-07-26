# -*- coding: utf-8 -*-
import scrapy_redis

# Scrapy settings for dgkey project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'dgkey'

SPIDER_MODULES = ['dgkey.spiders']
NEWSPIDER_MODULE = 'dgkey.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dgkey (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 8

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  ':authority': 'www.digikey.cn',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'upgrade-insecure-requests': '1',
    'cookie': 'i10c.uid=1560320222822:2140; _ga=GA1.2.102241263.1560320234; EG-U-ID=E5d757aee7-e572-4ccc-a7a9-52b396473e33; _gid=GA1.2.1284065162.1561347516; WC_PERSISTENT=2qR%2fcTj0QTNq1A7kLdTsgQ4w8ag%3d%0a%3b2019%2d06%2d23+22%3a54%3a11%2e602%5f1560559417090%2d263739%5f10001%5f7170901%2c%2d7%2cCNY%5f10001; sid=180144000318897030xKJI9ABWQRNM60A47LK2V4IOSVZVN2A3SIT1MLPFHZG3TPSBJYY2IBZ7LG4ZDKJPM; SC_ANALYTICS_GLOBAL_COOKIE=77690e030271486d8ab64760dff7de83|True; WC_SESSION_ESTABLISHED=true; WC_AUTHENTICATION_7170901=7170901%2c5tQsI2n3RBXR3w%2f8dME%2bUwBoJLs%3d; WC_ACTIVEPOINTER=%2d7%2c10001; i10c.ss=1561518106075; JSESSIONID=0003Doxb0E_nB3Gc_ar1MiDqhSp:-LOBC; rvps=7870435<SEP>7870373<SEP>7868572<SEP>7868697<SEP>7868902<SEP>7869214<SEP>7869885<SEP>7871480; TS01b442d5=01460246b674f8edcc2c0973025ac80018730f9c622775096e4750843a4df99bbc0104b072dbe97eb787d86d2d541c89eaa75e57af; DKLoggedIn=true; website#lang=zh-CN-RMB; dtCookie=9C0F262483BC3C59B0A337276796C1EA|X2RlZmF1bHR8MQ; TS01d239f3=01460246b6e51805a7c8223a5e532b40aef30764541cba9fcf261407360b32a0e99bc9043cf575e82c79d013b0bcf4f7f8183c6c36; TS01a4fc19=01460246b6e51805a7c8223a5e532b40aef30764541cba9fcf261407360b32a0e99bc9043cf575e82c79d013b0bcf4f7f8183c6c36; TS01c2873f=01460246b674f8edcc2c0973025ac80018730f9c622775096e4750843a4df99bbc0104b072dbe97eb787d86d2d541c89eaa75e57af; _gat_Production=1; WC_USERACTIVITY_7170901=7170901%2c10001%2cnull%2cnull%2c1561519756389%2c1564111905090%2cnull%2cnull%2cnull%2cnull%2c7PUG5ZgxQrqwAtbYSL0PbqBNnH1eKH%2fpmgkCKEaU%2bJh1z%2bAlJzbm%2brgaujNbL1DFQMCFQTVurxAQ%0a%2bb1t8PpRIhOs%2fE%2fCvpDKI0LlS8%2fNfvb3KkbUACCIP8uBJsOdY%2bZ9BDPJNLFTIQNyh7nwz1oWNWXs%0amqOUP%2fCfb26h10JLmno%3d; EG-S-ID=A7b42af33a-eedb-4a86-b715-a832d521337f; i10c.uservisit=292; utag_main=v_id:016b4a5544dc009d28a97567838003072005f06a00bd0$_sn:17$_ss:0$_st:1561521724156$ses_id:1561518107026%3Bexp-session$_pn:8%3Bexp-session'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'dgkey.middlewares.DgkeySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'dgkey.middlewares.ProxyMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'dgkey.pipelines.DgkeyPipeline': 300,
}


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
AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# FEED_EXPORT_FIELDS = [""]
FEED_EXPORT_ENCODING = 'UTF-8-SIG'
filename = input('数据文件名称： ')

DOWNLOAD_TIMEOUT = 10

SCHEDULER = "scrapy_redis.scheduler.Scheduler"

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

SCHEDULER_PERSIST = True

# REDIS_URL = 'redis://root@192.168.0.155:6379'

# REDIS_HOST = '192.168.0.155'
# # 端口为数字
# REDIS_PORT = 6379
