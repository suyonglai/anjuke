# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import redis

#from scrapy.conf import settings
from scrapy.utils.project import get_project_settings
settings=get_project_settings()
class MongoDBPipeline(object):

    def __init__(self):
        host='localhost'
        port=27017
        db_name='anjuke'
        client = pymongo.MongoClient(host=host,port=port)
        db=client[db_name]
        collection_name='houses'
        self.mycol=db[collection_name]


    def process_item(self, item, spider):

        self.mycol.insert_one(dict(item))
        return item

class XiciProxyPipeline(object):
    def open_spider(self,spider):
        if spider.name=="xici":
            host=settings.get("REDIS_HOST")
            port=settings.get("REDIS_PROT")
            db_index=settings.get("REDIS_DB_INDEX")
            self.db_conn=redis.StrictRedis(host=host,
                                           port=port,
                                           decode_responses=True)
            #self.db_conn.delete("ip")
    def process_item(self,item,spider):
        if spider.name=="xici":
            item_dict=dict(item)
            self.db_conn.sadd("ip",item_dict["url"])
        return item