# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DivescrapebotItem(scrapy.Item):
    when = scrapy.Field()
    location = scrapy.Field()
    depth = scrapy.Field()
    pass
