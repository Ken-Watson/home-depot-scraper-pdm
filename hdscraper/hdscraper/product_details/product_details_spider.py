"""Spider to scrape Home Depot product data using a GUI where the user can select categories"""
import scrapy
from scrapy.crawler import CrawlerProcess
from items import HdscraperProductItems


class ProductSpider(scrapy.Spider):
    """
    Scrapy spider class that defines the behavior of the spider for scraping
    product data from the Home Depot website.
    """

    name = "detailsspider"

    def start_requests(self):
        urls = []
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={"myarg": "value"})

    def parse(self, response, **kwargs):
        for product_url in response.css("a.product::attr(href)").getall():
            yield scrapy.Request(url=product_url, callback=self.parse_product)

    def parse_product(self, response):
        """Parse product details page"""
        product = HdscraperProductItems()

        product["name"] = response.css("h1.product-title::text").get().strip()
        product["sku"] = response.css("span.price::text").get().strip()
        product["price"] = response.css("span.price::text").get().strip()
        product["description"] = (
            response.css("div.product-description::text").get().strip()
        )
        product["category"] = response.meta["myarg"]
        product["url"] = response.url

        yield product


def start_scrapy(category_links):
    """Start scrapy process"""
    for link in category_links:
        process = CrawlerProcess(
            {
                "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                "FEED_FORMAT": "json",
                "FEED_URI": "output.json",
                "START_URLS": [link],
            }
        )
        process.crawl(ProductSpider)
        process.start()
