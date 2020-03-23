# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Movie1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = 'movie_url'
    href = scrapy.Field()
    title = scrapy.Field()