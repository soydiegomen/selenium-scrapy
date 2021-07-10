# Scrapy settings for openaq project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'openaq'

SPIDER_MODULES = ['openaq.spiders']
NEWSPIDER_MODULE = 'openaq.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

BOT_NAME = 'openaq'

SPIDER_MODULES = ['openaq.spiders']
NEWSPIDER_MODULE = 'openaq.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'openaq.pipelines.SaveProductsPipeline': 100,
    #'openaq.pipelines.DuplicatesPipeline': 100,
    #'openaq.pipelines.SaveQuotesPipeline': 200,
}

#CONNECTION_STRING = 'sqlite:///scrapy_quotes.db'
CONNECTION_STRING = 'mysql+mysqlconnector://root:root@localhost:8889/scrapy_test_db'


#DMG Unable the logs
#LOG_ENABLED=False