# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ImgspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class ImgPipeline(object):

    def __init__(self):
        self.file = open('imgs.txt', 'w')

    def process_item(self, item, spider):
        url = dict(item)['img_url'] + "\n"

        self.file.write(url)

        return item
