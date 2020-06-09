# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy import Request
from ..items import AnjukeItem
import time
import re
import myxici
import random


# curtpage = 2
'''class AnjukespiderSpider(scrapy.Spider):
    name = 'anjukeSpider'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://heb.anjuke.com/sale/shuangchengs/']'''
#读取带读取的url列表，urls.txt 由另一个文件爬取生成
with open('urls.txt') as f:
    ulr_list = f.readlines()
f.close()
cookie='Paat_2132_saltkey=z5CaGvzA; Paat_2132_lastvisit=1591439478; Paat_2132_forum_lastvisit=D_62_1591443107; Paat_2132_visitedfid=62; Paat_2132_viewid=tid_133040; Paat_2132_sid=m09uNc; Paat_2132_st_p=0%7C1591714042%7C033b90838e2f03ee8ff460154c824cfe; Paat_2132_sendmail=1; Paat_2132_lastact=1591714042%09plugin.php%09'

class syl_spider(RedisSpider):
    name='syl_spider'
    #allowed_domains = ['anjuke.com']
    #redis_key = 'syl_spider:start_urls'
    #start_urls = ['https://hrb.58.com/huochec/0/pve_11462_2017_2019/']
    def parse(self, response):
        try:
            item = AnjukeItem()
            item['title'] = response.xpath('//*[@id="thread_subject"]/text()').extract()[0]
            str = ''
            content_tmp = response.xpath('//*[@class="t_f"]/text()').extract()
            for i in content_tmp:
                str=str+i
            item['content'] = str
            item['phone'] = re.findall('[0-9]{11}', str)[0]

            yield item
        except:
            print('found a error!!!')
        for url in ulr_list:
            try:
                yield scrapy.Request(url[:-1],cookies=cookie,dont_filter=True)
                time.sleep(random.randint(30,70))
                # proxy=random.choice(myxici.get_myurl())
                # yield scrapy.Request(url[:-1],callback=self.parse,errback=self.error_back,meta={"proxy":proxy,"download_timeout":20})
            except:
                print('可能是超时了')
    #def error_back(self,failure):
            #pass
            #print('这个IP不可用，看看下一个吧')



'''def parse(self, response):
        try:
            houses=response.xpath('//ul[@class="car_list"]/li')
            for each_house in houses:
                item=AnjukeItem()
                item['title']=each_house.xpath('div[2]/a/h2/text()').extract()[0]
                item['year']=each_house.xpath('div[2]/div[1]/span[2]/text()').extract()[0].split()[0]
                item['distance']=each_house.xpath('div[2]/div[1]/span[3]/text()').extract()[0].split()[0]
                #item['price']=each_house.xpath('div[3]/h3/i/text()').extract()[0].split()[0]
                item['url']=each_house.xpath('div[2]/a/@href').extract()[0].split()[0]

                yield item
        except:
            print('found a error!!!')

        with open('58url.txt') as f:
            ulr_list=f.readlines()
        for url in ulr_list:

             url_next="https://"+url+"/huochec/0/pve_11462_2017_2019/"

             time.sleep(90)

             yield scrapy.Request(url_next)
        f.close()'''











'''           try:
                        str=''
                             
                        content_tmp=response.xpath('//*[@class="t_f"]/text()').extract()
                        for i in content_tmp:
                            #str=str+i
                        item['content'] =str
                        item['phone'] = re.findall('[0-9]{11}',str)[0]
                        yield item
                    except:
                        print('found a error!!!')
            
                    with open('urls1.txt') as f:
                        ulr_list=f.readlines()
                        print(ulr_list)
                    f.close()
                    for url in ulr_list:
                        yield scrapy.Request(url)
           time.sleep(5)  '''



