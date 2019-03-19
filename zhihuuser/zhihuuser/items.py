# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class UserItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = Field()
    name = Field()
    headline = Field()
    gender = Field()
    follower_count = Field()
    type = Field()
    url_token = Field()
    url = Field()
    badge = Field()
    avatar = Field()
    answer_count = Field()
    article_count = Field()
    user_type = Field()