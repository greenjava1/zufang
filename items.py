# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZufangItem(scrapy.Item):
    size = scrapy.Field()
    title = scrapy.Field()
    money = scrapy.Field()
    floor = scrapy.Field()
    #head = scrapy.Field()
    #age = scrapy.Field()
    name = scrapy.Field()
    #location = scrapy.Field()
    # define the fields for your item here like:
    pass
