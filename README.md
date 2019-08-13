# Python 3 Spider

* `1688item - distributed` : 利用ip代理池+分布式爬取阿里巴巴目标商家的信息，阿里巴巴限制每个ip的访问次数，所以需要用到ip 代理池，同时需要带cookie 访问。

* `KFC` : 肯德基官网获取全国范围内开设餐厅的城市省份，根据结果爬取所有餐厅的信息，存为Excel，并将结果标注在全国地图上。

* `bilibiliComments` : 对B站的视频的弹幕进行爬取，jieba分词，WordCloud生成词云图片。

* `dgkey-distributed` : scrapy-redis 分布式爬取 digekey 网站的电子元器件信息，保存为本地csv文件，图片按日期下载保存。

* `dotamax` : app 爬虫，利用 charles 抓包夜神模拟器的上 MAX+ ，获取对应的 url 后伪装手机客户端请求 header 利用 requests 库请求，获得的响应是 json 格式的数据，处理后获取 dota2 的全部英雄信息。

* `doubanSpider` : 根据含有书名的Excel文件逐条查找补充书目信息，爬取豆瓣上的出版社、出版时间、ISBN、定价、评分、评分人数等；整合到pandas进行简单分析。

* `taobaoItems` : 爬取淘宝的物品信息，将物品的店名，付款人数，地区，是否包邮，价格，详情页等信息爬取后保存为Excel文件。
  
* `WechatArticles`: 利用搜狗爬取微信文章的爬取。
 
* `weiboSearchScrapy` ：运用 cookie 池，爬取相关关键字微博的信息，微博反爬是判断的账号的，因此需要准备多个账号的cookie，当账号被屏蔽时，需要从cookies 池提取新的可用 cookie。

* `zhihuUserScrapy` : 基于Scrapy框架，设定一个用户为起点，获取关注和粉丝列表，然后同样遍历获得的用户。


