# -*- coding: utf-8 -*-
import requests
import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy import Request
#from anjuke.items import AnjukeItem
import re
import lxml
import time
urls=[]
for i in range(1, 80):
    urllist = 'https://www.fuxianhu.com/forum-62-' + str(i) + '.html'

    url_respons = requests.get(urllist).content.decode()
    #print(url_respons)
    url_20 =re.findall(r'<a href=\"thread(.*?)\.html\" onclick=\"atarget',url_respons)
    for url_one in url_20:
            urls.append('https://www.fuxianhu.com/thread' +url_one + '.html'+'\n')
    with open('urls.txt', 'w') as f:
                f.writelines(urls)
                f.close()
    time.sleep(3)
    print('正在采集第{}页。。。',i)
            #yield scrapy.Request(url)'''