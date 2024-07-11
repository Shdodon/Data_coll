# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class UnsplItem(Item):
    name_image = scrapy.Field()
    featured_in = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()