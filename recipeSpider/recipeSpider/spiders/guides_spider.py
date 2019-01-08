from scrapy import Request
from scrapy.spiders import Spider
from recipeSpider.items import GuidespiderItem


class RecipeSpider(Spider):
    name = 'ifixit'
    # allowed_domains = ["ifixit.com"]
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'en',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
    }

    def start_requests(self):
        devices = ['Apparel', 'Appliance', 'Camera', 'Car and Truck', 'Computer Hardware', 'Electronics', 'Game Console', 'Household', 'iPod', 'Mac', 'Media Player', 'PC', 'Phone', 'Skills', 'Tablet', 'Vehicle']
        for i in range(0, 16):
            url = 'https://www.ifixit.com/Device/' + devices[i]
            yield Request(url, headers=self.headers)

    def parse(self, response):
        categories = response.xpath('//div[@class="categoryListCell"]/a/@href').extract()
        if categories:
            for category in categories:
                url = 'https://www.ifixit.com' + category
                yield Request(url, callback=self.parse, headers=self.headers)
        else:
            guides = response.xpath('//div[@class="cell"]/a/@href').extract()
            for guide in guides:
                print(guide)
                url = 'https://www.ifixit.com' + guide
                yield Request(url, callback=self.parse_content, headers=self.headers)


    def parse_content(self, response):
        item = GuidespiderItem()
        step_list = response.xpath('//p[@itemprop="text"]/text()').extract()
        item['guide'] = step_list
        if item['guide']:
            yield item
