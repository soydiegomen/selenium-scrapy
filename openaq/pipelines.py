# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
import logging

from sqlalchemy.sql.elements import Null
from openaq.spiders.models import Quote, Author, Tag, db_connect, create_table

def setup_logger():
    logger = logging.getLogger('scrapper_app')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('scrapper_app.log')
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    return logger

class DuplicatesPipeline(object):
    logger = None
    session = None

    def __init__(self):
        self.logger = setup_logger()
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        exist_quote = session.query(Quote).filter_by(quote_content = item["quote_content"]).first()

        if exist_quote is not None:  # the current quote exists
            raise DropItem("Duplicate item found: %s" % item["quote_content"])
            session.close()
        else:
            return item
            session.close()

class SaveQuotesPipeline(object):
    logger = None
    session = None

    def __init__(self):
        self.logger = setup_logger()
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)


    def process_item(self, item, spider):
                
        session = self.Session()
        quote = Quote()
        author = Author()
        tag = Tag()
        author.name = item["author_name"]
        author.birthday = item["author_birthday"]
        author.bornlocation = item["author_bornlocation"]
        author.bio = item["author_bio"]
        quote.quote_content = item["quote_content"]
        self.logger.info('#Saving Quote: {}'.format(item["quote_content"]) )

        # check whether the author exists
        exist_author = session.query(Author).filter_by(name = author.name).first()
        if exist_author is not None:  # the current author exists
            quote.author = exist_author
        else:
            quote.author = author

        # check whether the current quote has tags or not
        if "tags" in item:
            for tag_name in item["tags"]:
                tag = Tag(name=tag_name)
                # check whether the current tag already exists in the database
                exist_tag = session.query(Tag).filter_by(name = tag.name).first()
                if exist_tag is not None:  # the current tag exists
                    tag = exist_tag
                quote.tags.append(tag)

        try:
            session.add(quote)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item
