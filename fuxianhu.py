# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy import Request
from anjuke.items import AnjukeItem
import re

#curtpage = '133036'
'''class AnjukespiderSpider(scrapy.Spider):
    name = 'anjukeSpider'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://www.fuxianhu.com/thread-133037-1-1.html']'''

class syl_spider(RedisSpider):
    name='syl_spider'
    #allowed_domains = ['anjuke.com']
    #redis_key = 'syl_spider:start_urls'
    #start_urls = ['https://www.fuxianhu.com/thread-133038-1-1.html']



    def parse(self, response):

            item=AnjukeItem()
            item['title']=response.xpath('//*[@id="thread_subject"]').extract()[0]
            item['content']=re.search('postmessage_[0-9]{6}>(.*?)</td>',response)
            item['phone']=re.search('[0-9]{11}')
            #item['price']=each_house.xpath('div[3]/h3/i/text()').extract()[0].split()[0]
            #item['url']=each_house.xpath('div[2]/a/@href').extract()[0].split()[0]
            yield item

    for i in range(1,79):
        urllist='https://www.fuxianhu.com/forum-62-'+i+'.html'
        url_respons=scrapy.Request(urllist)
        for each_url in url_respons:
            url_20=each_url.xpath('//*[@id="moderate"]')
            for url_one in url_20:
                url=url_one.xpath('table/tbody/tr/th/a[2]/@href').extract()[0].split()[0]
                yield scrapy.Request(url)



         #for curtpage in range(12,31):

         #   url_next='https://heb.anjuke.com/sale/echeng/p'+str(curtpage)+'/#filtersort'

         #    yield scrapy.Request(url_next)
