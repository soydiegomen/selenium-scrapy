import scrapy

class ClothingstoreSpider(scrapy.Spider):
    name = "common_spider"
    start_urls = ['https://www.pullandbear.com/mx/rebajas/hombre/favoritos-n6705']

    def parse(self, response):
        filename = f'page-result.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')