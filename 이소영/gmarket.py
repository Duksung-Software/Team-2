import scrapy


class GmarketSpider(scrapy.Spider):
    name = 'gmarket'
    allowed_domains = ['browse.gmarket.co.kr']
    start_urls = ['http://browse.gmarket.co.kr/']

    def parse(self, response):
        pass
