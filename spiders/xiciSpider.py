#-*-coding:utf-8-*-
from scrapy import Request
from scrapy.spiders import Spider
from ..items import  XiciProxyItem

class XiciSpider(Spider):
    name='xici'

    def __init__(self,url):
        self.test_url=url
        self.current_page=1

    def start_requests(self):
        url='https://www.xicidaili.com/nn'
        yield Request(url)

    def parse(self, response):
        list_selector=response.xpath("//tr[@class='odd']")
        for one_selector in list_selector:
            item=XiciProxyItem()
            ip=one_selector.xpath("td[2]/text()").extract()[0]
            port=one_selector.xpath("td[3]/text()").extract()[0]
            http=one_selector.xpath("td[6]/text()").extract()[0]
            url="{}://{}:{}".format(http,ip,port)
            item["url"]=url
            yield Request(self.test_url,
                          callback=self.test_parse,
                          errback=self.error_back,
                          meta={"proxy":url,
                                "dont_retry":True,
                                "download_timeout":10,
                                "item":item},
                          dont_filter=True
            )
        if self.current_page<=5:
            next_url=response.xpath("//a[@class='next_page']/@href").extract()[0]
            next_url=response.urljoin(next_url)
            self.current_page+=1
            yield Request(next_url)

    def test_parse(self,response):
        yield response.meta["item"]
    def error_back(self,failure):
        self.logger.error(repr(failure))


