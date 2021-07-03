import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logzero import logfile, logger


class CountriesSpiderSpider(scrapy.Spider):

    # Initializing log file
    logfile("openaq_spider.log", maxBytes=1e6, backupCount=3)
    name = "webapp_spider"
    allowed_domains = ["toscrape.com"]

    # Using a dummy website to start scrapy request
    def start_requests(self):
        url = "http://quotes.toscrape.com"
        yield scrapy.Request(url=url, callback=self.parse_webapp)

    def parse_webapp(self, response):
        # driver = webdriver.Chrome()  # To open a new browser window and navigate it

        # Use headless option to not open a new browser window
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        desired_capabilities = options.to_capabilities()
        driver = webdriver.Chrome(desired_capabilities=desired_capabilities)

        # Getting list of Countries
        driver.get("http://quotes.toscrape.com")

        # Implicit wait
        driver.implicitly_wait(10)

        # Explicit wait
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "card-body")))

        # Extracting country names
        countries = driver.find_elements_by_class_name("text-lighter")
        countries_count = 0
        # Using Scrapy's yield to store output instead of explicitly writing to a JSON file
        for country in countries:
            yield {
                "feature": country.text,
            }
            countries_count += 1

        driver.quit()
        logger.info(f"Total de items: {countries_count}")
