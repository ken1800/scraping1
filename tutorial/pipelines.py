# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class MongodbPipeline(object):
    # def process_item(self, item, spider):
    #     return item
    #collection_name = 'quotes'
    collection_name = 'quotes'

    def __init__(self):
         self.mongo_uri = 'mongodb://localhost:27017'
         self.mongo_db = 'goodreads'
        

    
    def open_spider(self, spider):
         self.client = pymongo.MongoClient(self.mongo_uri)
         self.db = self.client[self.mongo_db]
       
    
    # @classmethod
    # def from_crawler(cls, crawler):
    #     # return cls(
    #     #     mongo_uri=crawler.settings.get('MONGO_URI'),
    #     #     mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
    #     # )
    #     pass


    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item