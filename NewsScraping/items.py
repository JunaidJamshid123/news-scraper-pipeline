# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy



class NewsArticleItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    date = scrapy.Field()
    author = scrapy.Field()
    imageUrl = scrapy.Field()
    publication = scrapy.Field()
    category = scrapy.Field()
    url = scrapy.Field()
    location = scrapy.Field()
    date = scrapy.Field()  # Ensure this line is present
    biasness = scrapy.Field(default="central")  # Added biasness field with default value
    score = scrapy.Field(default="0")  # Added biasness field with default value