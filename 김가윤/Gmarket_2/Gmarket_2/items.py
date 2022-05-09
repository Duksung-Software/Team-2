# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Gmarket2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Name = scrapy.Field()
    Price = scrapy.Field()
    Delivery_charge = scrapy.Field()
    URL = scrapy.Field()
