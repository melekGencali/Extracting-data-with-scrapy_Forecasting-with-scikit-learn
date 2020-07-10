# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyprojeItem(scrapy.Item):
    # define the fields for your item here like:


    baslik = scrapy.Field()
    kategori = scrapy.Field()
    fiyat = scrapy.Field()
    features = scrapy.Field()
    yildiz = scrapy.Field()
    yorum = scrapy.Field()
    yorumYildizi = scrapy.Field()
    yonetmen = scrapy.Field()
    oyuncular = scrapy.Field()

    pass
