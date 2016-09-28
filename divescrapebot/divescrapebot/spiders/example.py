# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["www.en.divelogs.de"]
    start_urls = (
        'http://www.www.en.divelogs.de/',
    )

    def parse(self, response):
        pass
