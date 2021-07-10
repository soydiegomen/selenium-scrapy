import scrapy

class ClothingstoreSpider(scrapy.Spider):
    name = "common_spider"
    #Dinamica
    #start_urls = ['https://www.pullandbear.com/mx/rebajas/hombre/favoritos-n6705']
    #Estatica
    #start_urls = ['https://www.lotherington.mx/liquidaci%C3%B3n']
    #start_urls = ['https://malinali.store/collections/all']
    #start_urls = ['https://libreliebre.com/collections/playeras-para-mujer']
    #start_urls = ['https://malandro.mx/collections/tshirts']
    #start_urls = ['https://malandro.mx/collections/tshirts']
    start_urls = ['https://nataliaa-artwork.company.site/']

    def parse(self, response):
        filename = f'page-result-malandro.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')