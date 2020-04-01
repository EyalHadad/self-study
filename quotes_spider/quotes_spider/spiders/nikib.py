# -*- coding: utf-8 -*-
import scrapy


class NikibSpider(scrapy.Spider):
    name = 'nikib'
    allowed_domains = ['nikib.co.il/cakes-dessert/chocolate-cakes/3747']
    start_urls = ['https://foody.co.il/foody_recipe/%d7%a9%d7%91%d7%9c%d7%95%d7%9c%d7%99-%d7%a9%d7%9e%d7%a8%d7%99%d7%9d-%d7%91%d7%9e%d7%9c%d7%99%d7%aa-%d7%a9%d7%95%d7%a7%d7%95%d7%9c%d7%93-%d7%a9%d7%9c-%d7%99%d7%94%d7%95%d7%93%d7%99%d7%aa-%d7%9e%d7%95/']

    def parse(self, response):
        pass
