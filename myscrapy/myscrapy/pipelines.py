# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyscrapyPipeline(object):
    def process_item(self, item, spider):
        with open("my_jd.txt", "a", encoding='utf-8') as fp:
            fp.write(''.join(item['name']) + "\n" + "https:" + ''.join(item['url']) + "\n" + ''.join(item['price']) + "\n")
        return item
