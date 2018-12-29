import scrapy
# scrapy runspider scrapper_character.py -o s_characters.json
# -*- coding: utf8 -*-
import scrapy
class characterSpider(scrapy.Spider):
    name = 'characters'
    start_urls = ['https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Personnage_d%27animation']

    def parse(self, response):
        for characters in response.css('div#mw-pages div.mw-category li'):
            yield {'character': characters.css('a ::text').extract_first()}

