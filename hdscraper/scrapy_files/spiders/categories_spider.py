# """
# Scrapy crawl spider class that goes to the site map page
# and extracts all category names and links.
# """

# import re
# import scrapy

# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
# from ..items import HdscraperCategoryItem


# class CategorySpider(CrawlSpider):
#     """
#     Scrapy crawler class that goes to the site map page and extracts all
#     category links.
#     """

#     name = "categoryspider"
#     allowed_domains = ["homedepot.com"]
#     start_urls = ["https://www.homedepot.com/c/site_map"]

#     # Define a tuple of rules to be followed by the spider.
#     rules = (
#         Rule(
#             # Define the LinkExtractor to use for this rule.
#             LinkExtractor(
#                 # Deny URLs that match the regular expressions in this tuple.
#                 deny=(r"\n\t\t\t\t\t\t\t", r"^\/b"),
#                 # Restrict to elements matching the XPath expressions in this tuple.
#                 restrict_xpaths=("//div[@class='content experience']",),
#             ),
#             # Use the parse_category method as the callback for this rule.
#             callback="parse_category",
#             # Don't follow links on the page.
#             follow=False,
#         ),
#     )

#     # pylint: disable=W0221
#     def parse(self, response):
#         """
#         Default callback used by Scrapy to process responses.
#         Override this method to handle the response and extract data.
#         """
#         return self.parse_category(response)

#     def parse_category(self, response):
#         """Parse category links."""
#         # item = HdscraperCategoryItem()

#         # seen_urls = set()
#         # for link in response.css("a[href*='https://www.homedepot.com/b/']"):
#         #     # Skip links that don't match the given regular expression
#         #     if not re.match(
#         #         r"https://www\.homedepot\.com/b/[^/]+/N-[a-zA-Z0-9]+/?$",
#         #         link.attrib["href"],
#         #     ):
#         #         continue
#         #     category_link = link.css("::attr(href)").get()
#         #     # If the URL has not been seen before, add it to the set of seen URLs
#         #     if category_link not in seen_urls:
#         #         seen_urls.add(category_link)
#         #         if link.css("::text").get().strip():
#         #             item["category"] = link.css("::text").get().strip()
#         #             item["url"] = category_link + "?catStyle=ShowProducts"

#         #             # Yield the item to be processed in pipelines.py
#         #             yield item

#         items = []

#         seen_urls = set()
#         for link in response.css("a[href*='https://www.homedepot.com/b/']"):
#             # Skip links that don't match the given regular expression
#             if not re.match(
#                 r"https://www\.homedepot\.com/b/[^/]+/N-[a-zA-Z0-9]+/?$",
#                 link.attrib["href"],
#             ):
#                 continue
#             category_link = link.css("::attr(href)").get()
#             # If the URL has not been seen before, add it to the set of seen URLs
#             if category_link not in seen_urls:
#                 seen_urls.add(category_link)
#                 if link.css("::text").get().strip():
#                     item = HdscraperCategoryItem()
#                     item["category"] = link.css("::text").get().strip()
#                     item["url"] = category_link + "?catStyle=ShowProducts"
#                     items.append(item)

#         # Sort the items in alphabetical order by category
#         sorted_items = sorted(items, key=lambda x: x["category"])

#         # Yield the sorted items one by one
#         for item in sorted_items:
#             yield item

