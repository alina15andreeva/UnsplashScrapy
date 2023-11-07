import scrapy
from scrapy.http import HtmlResponse
from sys import path

path.append('/Users/alinaandreeva/Downloads/practice6/unsplashparser')
from items import UnsplashparserItem
from scrapy.loader import ItemLoader


class UnsplashSpider(scrapy.Spider):
    name = "unsplash"
    allowed_domains = ["unsplash.com"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f"https://unsplash.com/s/photos/{kwargs.get('query')}"]

    def parse(self, response: HtmlResponse):
        links = response.xpath("//div[@class='mItv1']//a[@itemprop]")
        for link in links:
            yield response.follow(link, callback=self.parse_pic)

    def parse_pic(self, response:HtmlResponse):

        loader = ItemLoader(item=UnsplashparserItem(), response=response)
        loader.add_xpath('name', "//div[@class='MorZF']//@alt")
        loader.add_xpath('category', "//div[@class='VZRk3 rLPoM']//@title")
        loader.add_value('url', response.url)
        loader.add_xpath('photos', "//div[@class='MorZF']//@srcset")

        yield loader.load_item()
