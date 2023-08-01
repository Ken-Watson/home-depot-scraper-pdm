import scrapy

class CategorySpider(scrapy.Spider):
    name = "categoryspider"
    start_urls = [
        "https://www.homedepot.com/c/site_map"  # Replace with the sitemap URL
    ]

    def __init__(self, chosen_categories=None, *args, **kwargs):
        super(CategorySpider, self).__init__(*args, **kwargs)
        self.chosen_categories = chosen_categories or []

    def parse(self, response):
        # Extract links to top-level categories from the sitemap
        category_links = response.css("a.category-link::attr(href)").getall()

        # Filter category links based on the chosen categories
        filtered_links = [link for link in category_links if self.is_chosen_category(link)]

        # Follow links to top-level categories
        yield from response.follow_all(filtered_links, self.parse_category)

    def parse_category(self, response):
        # Extract subcategories and follow links to deeper subcategories
        subcategory_links = response.css("a.subcategory-link::attr(href)").getall()
        yield {
            "category": response.url,
            "subcategories": [response.urljoin(link) for link in subcategory_links],
        }

    def is_chosen_category(self, link):
        # Check if the link corresponds to a chosen category
        return any(category in link for category in self.chosen_categories)
