# -*- coding: utf-8 -*-
import scrapy


class A10dakotSpider(scrapy.Spider):
    name = '10dakot'
    allowed_domains = [
        'hashulchan.co.il']
    start_urls = [
        'https://www.hashulchan.co.il/topic/%d7%90%d7%a4%d7%99%d7%99%d7%94/']

    def parse(self, response):
        links = response.xpath('//*[@class="template-item-image"]/a/@href').extract()
        for link in links:
            new_path = response.urljoin(link)
            yield scrapy.Request(link, callback=self.parse_recipe)

    def parse_recipe(self, response):
        ing_names = response.xpath('//*[@class="ing-name"]/text()').extract()
        title = response.xpath('//head//title/text()').extract_first()
        print("\n\nlink: ")
        print(str(response))
        yield {'Title': title,
               'Ing_Names': ing_names,
               'Link': str(response)
               }
