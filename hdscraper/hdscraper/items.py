# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HdscraperCategoryItem(scrapy.Item):
    category = scrapy.Field()
    url = scrapy.Field()


class HdscraperProductItems(scrapy.Item):
    name = scrapy.Field()
    sku = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    category = scrapy.Field()
    url = scrapy.Field()
