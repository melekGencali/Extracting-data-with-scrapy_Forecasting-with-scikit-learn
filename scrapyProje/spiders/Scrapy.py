# -*- coding: utf-8 -*-

import scrapy
from urllib.parse import urlparse
from urllib.parse import urljoin



from scrapyProje.items import ScrapyprojeItem



class ScrapySpider(scrapy.Spider):

    name = 'Scrapy'
    allowed_domains = ['fullhdfilmizlesene.com']

    start_urls = [

                  'https://www.fullhdfilmizlesene.com/filmizle/aile-filmleri-izle',
                  'https://www.fullhdfilmizlesene.com/filmizle/aile-filmleri-izle/2',
                  'https://www.fullhdfilmizlesene.com/filmizle/aile-filmleri-izle/3',
                  'https://www.fullhdfilmizlesene.com/filmizle/aile-filmleri-izle/4',
                  'https://www.fullhdfilmizlesene.com/filmizle/aile-filmleri-izle/5',
                  'https://www.fullhdfilmizlesene.com/filmizle/aile-filmleri-izle/6',
                  'https://www.fullhdfilmizlesene.com/filmizle/aile-filmleri-izle/7',
                  'https://www.fullhdfilmizlesene.com/filmizle/aile-filmleri-izle/8',
                  'https://www.fullhdfilmizlesene.com/filmizle/aile-filmleri-izle/9',
                  'https://www.fullhdfilmizlesene.com/filmizle/aile-filmleri-izle/10',


    ]

    def parse(self, response):
        print('Page URL: ' + response.url)



        for url in response.css('h2>a::attr(href)').getall():
            print('requesting: ' + url)

            yield scrapy.Request(url, callback=self.parseData)





    def parseData(self, response):
        item = ScrapyprojeItem()

        #item['baslik'] = response.css('h1>a::text').get()
        item['yildiz'] = response.css('div.rating>span::text').get()
        item['kategori']=response.css('dl>dd>a::text').extract()
        #item['yorum'] = response.css('ul>li>p::text').getall()
        #for content in  response.css('ul.film-yorumlist'):
        item["oyuncular"] = response.xpath('.//dl[dt/text()="Oyuncular"]/dd/text()').extract()[0]

        for scope in response.xpath('//div[@itemscope]'):


            for property in scope.xpath('//*[@itemprop="director"]//*[@itemprop="name"]'):

                item["yonetmen"]=property.xpath('string(.)').extract()[0]
                #print("icerik2",property.xpath('@*').extract())
        yield item


