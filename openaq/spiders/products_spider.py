import scrapy
import logging
from scrapy.loader import ItemLoader
from openaq.items import ProductItem

class ProductsSpider(scrapy.Spider):
    name = "products_spider"
    start_urls = ['https://nataliaa-artwork.company.site/']

    def parse(self, response):
        products = response.css('.grid-product__wrap-inner')
        logging.info("#Items4 {}".format(len(products)) )
        
        for product in products:
            loader = ItemLoader(item=ProductItem(), selector=product)
            #inner_product = product.css('.grid-product__title-inner::text')
            #logging.info("#product7 {}".format(inner_product.get()))
            loader.add_css('name', '.grid-product__title-inner::text')
            loader.add_css('price', '.grid-product__price-value::text')
            yield loader.load_item()