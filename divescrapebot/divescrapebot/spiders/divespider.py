import scrapy

class DiveSpider(scrapy.Spider):
    name = "divescrape"
    allowed_domains = ["en.divelogs.de"]
    start_urls = [
        "https://en.divelogs.de/log/drware/",
        "https://en.divelogs.de/log/henri61/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
