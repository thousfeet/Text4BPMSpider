from scrapy import Request
from scrapy.spiders import Spider
from recipeSpider.items import RecipespiderItem


class RecipeSpider(Spider):
    name = 'allrecipes'
    # allowed_domains = ["allrecipes.com"]
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'en',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
    }

    def start_requests(self):
        for i in range(1, 6):
            url = 'https://www.allrecipes.com/?page=' + str(i)
            yield Request(url, headers=self.headers)

    def parse(self, response):
        recipes = response.xpath('//div[@class="grid-card-image-container"]/a[1]/@href').extract()
        for recipe in recipes:
            print(recipe)
            yield Request(recipe, callback=self.parse_content, headers=self.headers)

    def parse_content(self, response):
        item = RecipespiderItem()
        step_list = response.xpath('//span[@class="recipe-directions__list--item"]/text()').extract()
        item['directions'] = step_list
        if item['directions']:
            yield item
