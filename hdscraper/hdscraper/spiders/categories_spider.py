"""
Scrapy crawl spider class that goes to the site map page
and extracts all category names and links.
"""

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CategoryCrawler(CrawlSpider):
    """
    Scrapy crawler class that goes to the site map page and extracts all
    category links.
    """

    name = "category_crawler"
    allowed_domains = ["homedepot.com"]
    start_urls = ["https://www.homedepot.com/c/site_map"]

    rules = (Rule(LinkExtractor(allow=("/b/",)), callback="parse_category"),)

    def __init__(self, *args, **kwargs):
        super(CategoryCrawler, self).__init__(*args, **kwargs)
        self.seen_urls = set()

    def parse_category(self, response):
        """Parse category links."""
        category_links = response.css("a[href*='/b/']::attr(href)").getall()
        for category_link in category_links:
            if category_link not in self.seen_urls:
                self.seen_urls.add(category_link)
                yield {
                    "category": response.css(
                        'a[href="' + category_link + '"]::text'
                    ).get(),
                    "url": category_link,
                }
        # category_links = response.css("a[href*='/b/']::attr(href)").getall()
        # for category_link in category_links:
        #     yield {
        #         "category": response.css('a[href="' + category_link + '"]::text').get(),
        #         "url": category_link,
        #     }
