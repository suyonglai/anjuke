# -*- coding: utf-8 -*-
import requests
import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy import Request
#from anjuke.items import AnjukeItem
import re
import lxml.html
import time
str=''
url='https://www.fuxianhu.com/thread-133025-1-1.html'
response = requests.get(url).content.decode()
sel = lxml.html.fromstring(response)
title=sel.xpath('//*[@id="thread_subject"]/text()')[0]
content_sel=sel.xpath('//*[@class="t_f"]/text()')
for i in content_sel:
    str=str+i
#content=content_sel.xpath('string(.)')
#content = re.findall('postmessage_[0-9]{6}>(.*?)</td>', sel)[0]
phone = re.findall(r'[0-9]{11}',str)[0]
print(title)
print(str)
print(phone)

time.sleep(3)
#print('正在采集第{}页。。。'.format(i))
            #yield scrapy.Request(url)'''