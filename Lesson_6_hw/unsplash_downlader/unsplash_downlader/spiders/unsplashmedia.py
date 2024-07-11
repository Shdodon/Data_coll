import scrapy
import os
from scrapy.loader import ItemLoader
from ..items import UnsplItem
from itemloaders.processors import MapCompose


class UnsplashmediaSpider(scrapy.Spider):
    name = "unsplashmedia"
    # allowed_domains = ["unsplash.com"]
    start_urls = ["https://unsplash.com/t/textures-patterns"]

    def parse(self, response):
        for image in response.xpath('//div[@class="d95fI"]/figure//div/a[@class="Prxeh"]/@href').extract():
            yield scrapy.Request(response.urljoin(image), self.parse_image)


    def parse_image(self, response):
        srcset_v = response.xpath('//div/button//div/img[@class="ApbSI z1piP vkrMA"]/@srcset').extract_first()
        images = [{'url': src.split(' ')[0], 'size': int(src.split(' ')[1].replace('w', ''))}
                  for src in srcset_v.split(', ')]
        size_image = min(images, key=lambda x: x['size'])
        if size_image:
            yield scrapy.Request(response.urljoin(size_image['url']), self.save_preview_image)

        image_all = max(images, key=lambda x: x['size'])
        if image_all:
            yield scrapy.Request(response.urljoin(image_all['url']), self.save_full_image)

        loader = ItemLoader(item=UnsplItem(), response=response)
        loader.default_input_processor = MapCompose(str.strip)

        loader.add_xpath('name_image', '//div[@class="VgSmN"]//div/h1/text()')

        categori_selectors = response.xpath('//div[@class="rx3zu _UNLg"]//div[@class="uK_kT"]/div//span/a/text()')
        categori = [s.get().strip() for s in categori_selectors if s.get().strip()]
        if categori:
            loader.add_value('featured_in', categori)

        loader.add_value('image_urls', size_image['url'])
        yield loader.load_item()

    def save_preview_image(self, response):
        self.save_image(response, 'preview_')

    def save_image_all(self, response):
        self.save_image(response, 'full_')

    def save_image(self, response, prefix):

        url_file_name = os.path.basename(response.url.split('?')[0])

        if not any(url_file_name.lower().endswith(ext) for ext in ['.jpg', '.png', '.jpeg']):
            url_file_name += '.jpg'
        file_name = f'{prefix}{url_file_name}'
        with open(f'images/{file_name}', 'wb') as f:
            f.write(response.body)