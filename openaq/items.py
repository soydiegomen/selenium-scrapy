# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst
from datetime import datetime


class OpenaqItem(scrapy.Item):
    country = scrapy.Field()
    city = scrapy.Field()
    location = scrapy.Field()
    pm25 = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()

#New code - Connectio so sqlite
def remove_quotes(text):
    # strip the unicode quotes
    text = text.strip(u'\u201c'u'\u201d')
    return text


def convert_date(text):
    # convert string March 14, 1879 to Python date
    return datetime.strptime(text, '%B %d, %Y')


def parse_location(text):
    # parse location "in Ulm, Germany"
    # this simply remove "in ", you can further parse city, state, country, etc.
    return text[3:]


class QuoteItem(Item):
    quote_content = Field(
        input_processor=MapCompose(remove_quotes),
        # TakeFirst return the first value not the whole list
        output_processor=TakeFirst()
        )
    author_name = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
        )
    author_birthday = Field(
        input_processor=MapCompose(convert_date),
        output_processor=TakeFirst()
    )
    author_bornlocation = Field(
        input_processor=MapCompose(parse_location),
        output_processor=TakeFirst()
    )
    author_bio = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
        )
    tags = Field()

class ProductItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()