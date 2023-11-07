# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from itemloaders.processors import TakeFirst, MapCompose, Compose

def process_name(value):
    value = value[0].strip()
    return value

def process_photo(value:str):
    value = value.split()[-2]
    return value


class UnsplashparserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor=Compose(process_name), output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    category = scrapy.Field()
    #photos = scrapy.Field(input_processor=MapCompose(process_photo))
    photos = scrapy.Field(input_processor=MapCompose(process_photo), output_processor=TakeFirst())
    _id = scrapy.Field()