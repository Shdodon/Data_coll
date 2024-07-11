# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class UnsplashDownladerPipeline:
#     def process_item(self, item, spider):
#         return item


import scrapy
from scrapy.pipelines.images import ImagesPipeline
import os

class UnsplashImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item.get('image_urls', []):
            yield scrapy.Request(image_url)

    def file_path(self, request, response=None, info=None, *, item=None):
        category = item.get('featured_in', ['unknown_category'])[0]
        image_name = os.path.basename(request.url.split('?')[0])
        return f"{category}/{image_name}"