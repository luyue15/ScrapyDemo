# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem


class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        movies = response.xpath('/html/body/div[6]/div[1]/ul/li/h5/a/@title').extract()

        for each_movie in movies:
            item = MovieItem()
            item['name'] = each_movie
            print(item['name'])
            yield item
