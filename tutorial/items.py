# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

def remove_quotations(value):
    return value.replace(u"\u201c", '').replace(u"\u201d", '')

class QuoteItem(scrapy.Item):
  text = scrapy.Field(
      input_processor=MapCompose(str.strip,remove_quotations),
      output_processor=TakeFirst(),
  )
  author = scrapy.Field(
    input_processor=MapCompose(remove_tags),
    output_processor = TakeFirst(),
  )
  
  tags = scrapy.Field(
    input_processor=MapCompose(remove_tags),
    output_processor = Join(',')
    
  )