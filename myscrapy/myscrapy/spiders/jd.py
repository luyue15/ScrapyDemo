# -*- coding: utf-8 -*-
import scrapy
from myscrapy.items import MyscrapyItem


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://search.jd.com/Search?enc=utf-8&page=1&keyword=坚果pro1100']
    start_urls = ['https://search.jd.com/Search?enc=utf-8&page=2&keyword=坚果pro1100']
    start_urls = ['https://search.jd.com/Search?enc=utf-8&page=3&keyword=坚果pro1100']
    start_urls = ['https://search.jd.com/Search?enc=utf-8&page=4&keyword=坚果pro1100']


    def parse(self, response):
        products = response.xpath('//*[@id="J_goodsList"]/ul/li')

        for each_item in products:
            item = MyscrapyItem()
            item['name'] = each_item.xpath('./div/div[4]/a/em/text()').extract()
            item['url'] = each_item.xpath('./div/div[4]/a/@href').extract()
            item['price'] = each_item.xpath('./div/div[3]/strong/i/text()').extract()
            print(item['name'])
            print(item['url'])
            print(item['price'])
            yield item
        pass
