import scrapy


class GMarketItem(scrapy.Item):
    Name = scrapy.Field()
    Price = scrapy.Field()
    Deliver_Charge = scrapy.Field()
    URL = scrapy.Field()
    pass
