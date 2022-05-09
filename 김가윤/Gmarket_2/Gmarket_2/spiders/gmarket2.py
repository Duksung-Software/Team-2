import scrapy
from Gmarket_2.items import Gmarket2Item

srhWord = input("검색어 입력 : ")
sortChoice = int(input("정렬 방식 선택 : 1. 판매 인기 순 / 2. 낮은 가격 순 / 3. 높은 가격 순 / 4. 상품평 많은 순 / 5. 신규 상품 순"))
sortNum = {1 : 8, 2 : 1, 3 : 2, 4 : 13, 5 : 3}
sorting = str(sortNum.get(sortChoice))

class Gmarket2Spider(scrapy.Spider):
    name = 'gmarket2'
    allowed_domains = ['browse.gmarket.co.']
    start_urls = ['http://browse.gmarket.co./search?keyword=' + srhWord + "&s=2" + sorting]

    def parse(self, response):

        global url
        for i in range(1,101):
            URL = response.xpath(f'//*[@id="section__inner-content-body-container"]/div[2]/div[{i}]/div[1]/div[2]/div[1]/div[2]/span/a')
            div = response.xpath(f'//*[@id="section__inner-content-body-container"]/div[2]/div[{i}]')
            if (URL != []):
                href = div.xpath('./div[1]/div[2]/div[1]/div[2]/span/a/@href')
                url = response.urljoin(href[0].extract())
                yield scrapy.Request(url, callback = self.parse_page_content1)

            if (URL == []):
                href = div.xpath('./div[1]/div[2]/div[1]/div[1]/span/a/@href')
                url = response.urljoin(href[0].extract())
                yield scrapy.Request(url, callback = self.parse_page_content2)

    def parse_page_content1(self, response) : 
        Price_str = response.xpath('//*[@id="itemcase_basic"]/div/p/span/strong/text()')[0].extract()
        Price_Num = Price_str.split(',')
        Price_List = ''.join(Price_Num)

        item = Gmarket2Item()
        item['Name'] = response.xpath('//*[@id="itemcase_basic"]/div/h1/text()')[0].extract()
        item['Price'] = response.xpath('//*[@id="itemcase_basic"]/div/p/span/strong/text()')[0].extract()
        item['Deliver_charge'] = response.xpath('//*[@id="container"]/div[3]/div[2]/div[2]/ul/li[1]/div[1]/div[2]/span/text()')[0].extract()
        item['URL'] = url
        return item

    def parse_page_content2(self, response) : 
        item = Gmarket2Item()
        item['Name'] = response.xpath('//*[@id="itemcase_basic"]/div/h1/text()')[0].extract()
        item['Price'] = response.xpath('//*[@id="itemcase_basic"]/div/p/span/strong/text()')[0].extract()
        item['Deliver_charge'] = response.xpath('//*[@id="container"]/div[3]/div[2]/div[2]/ul/li[1]/div[1]/div[2]/span/text()')[0].extract()
        item['URL'] = url
        return item
