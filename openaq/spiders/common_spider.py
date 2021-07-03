import scrapy

class ClothingstoreSpider(scrapy.Spider):
    name = "common_spider"
    start_urls = ['https://openaq.org/#/countries']

    def parse(self, response):
        filename = f'countries-page.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')