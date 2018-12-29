# scrapy runspider scrapper_quotes.py -o s_quotes.json
# -*- coding: utf8 -*-
import scrapy
class quoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://www.babelio.com/auteur/Frederic-Dard/7187/citations']

    def parse(self, response):
        for quote in response.css('div.post_con div.text.row div'):
            yield {'quote': quote.css('div ::text').extract()}