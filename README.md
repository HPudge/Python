# Python 3 项目

`Douban_comments` ：爬取豆瓣目标电影的评论，储存为csv文件，requests带参请求，re解析数据内容。

 `Maoyan_top100` : 对猫眼电影的 top100 榜单进行爬取，直接requests请求，re筛选目标内容，加入字典中，储存为txt文本。
 
 `TINY` : 是平时收集到的有趣或者使用的小玩意。
 
 `TouTiao_jiepai` : requests 带参数请求今日头条，获得json数据，修改获得的url数据可以直接用requests下载高清图片，储存到每个标题的文件夹中，多线程运行。
 
 `bilibilicoments` :     对哔哩哔哩的视频的弹幕进行爬取，获得弹幕文本后，利用jieba库对文本进行分词，分词后用WordCloud，matplotlib.pyplot词云图片
