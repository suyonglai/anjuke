# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy



class AnjukeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    content=scrapy.Field()
    phone=scrapy.Field()
    # price=scrapy.Field()
    #weight=scrapy.Field()
    #describe=scrapy.Field()
    #url=scrapy.Field()
class XiciProxyItem(scrapy.Item):
    url=scrapy.Field()