from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text, Numeric)
from scrapy.utils.project import get_project_settings

Base = declarative_base()

def db_connect():
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    Base.metadata.create_all(engine)


# Association Table for Many-to-Many relationship between Quote and Tag
# https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html#many-to-many
quote_tag = Table('quote_tag', Base.metadata,
    Column('quote_id', Integer, ForeignKey('quote.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)


class Quote(Base):
    __tablename__ = "quote"

    id = Column(Integer, primary_key=True)
    quote_content = Column('quote_content', Text())
    author_id = Column(Integer, ForeignKey('author.id'))  # Many quotes to one author
    tags = relationship('Tag', secondary='quote_tag',
        lazy='dynamic', backref="quote")  # M-to-M for quote and tag


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True)
    name = Column('name', String(50), unique=True)
    birthday = Column('birthday', DateTime)
    bornlocation = Column('bornlocation', String(150))
    bio = Column('bio', Text())
    quotes = relationship('Quote', backref='author')  # One author to many Quotes


class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True)
    name = Column('name', String(30), unique=True)
    quotes = relationship('Quote', secondary='quote_tag',
        lazy='dynamic', backref="tag")  # M-to-M for quote and tag

#DMG Models for test
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column('name', String(50))
    price = Column('price', Numeric(precision=8))
    detail_url = Column('detail_url', String(500))
    thumbnail_url = Column('thumbnail_url', String(500))
    comments = relationship("Comment", backref='product')


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    detail = Column('detail', String(500))
    product_id = Column(Integer, ForeignKey('products.id'))