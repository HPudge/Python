# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import requests
import time
import scrapy

from twisted.internet import defer
from twisted.internet.error import TimeoutError, DNSLookupError, \
    ConnectionRefusedError, ConnectionDone, ConnectError, \
    ConnectionLost, TCPTimedOutError

from twisted.web.client import ResponseFailed
from scrapy.core.downloader.handlers.http11 import TunnelError


class ProxyMiddleware(object):
    PROXY_POOL_URL = 'http://192.168.0.155:5010/get/'

    ALL_EXCEPTIONS = (defer.TimeoutError, TimeoutError, DNSLookupError,
                      ConnectionRefusedError, ConnectionDone, ConnectError,
                      ConnectionLost, TCPTimedOutError, ResponseFailed,
                      IOError, TunnelError, IndexError)

    def get_proxy(self):
        try:
            response = requests.get(self.PROXY_POOL_URL)
            if response.status_code == 200:
                return response.text
        except ConnectionError:
            time.sleep(30)
            self.get_proxy()

    def process_request(self, request, spider):
        proxy = self.get_proxy()

        request.meta['proxy'] = 'http://' + proxy

    def process_exception(self, request, exception, spider):
        if isinstance(exception, self.ALL_EXCEPTIONS):
            print('Got exception: %s' % exception)
            requests.get('http://192.168.0.155:5010/delete?proxy={}'.format(request.meta['proxy'][7:]))
            return scrapy.Request(request.url, meta=request.meta)


