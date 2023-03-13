# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import sqlite3

from itemadapter import ItemAdapter


class SqliteCategoryPipeline:
    """Pipeline for storing scraped items in the SQLite database."""

    def __init__(self):
        self.conn = None
        self.cursor = None

    @classmethod
    def from_crawler(cls, crawler):
        """Used to instantiate the pipeline object with any crawler-specific settings."""
        return cls()

    def open_spider(self, spider):
        """Open the connection to the database."""
        self.conn = sqlite3.connect("hdscraper.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def close_spider(self, spider):
        """Close the connection to the database."""
        self.conn.close()

    def create_table(self):
        """Create the table if it doesn't exist."""
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            category TEXT,
            url TEXT
            );"""
        )
        self.conn.commit()

    def process_item(self, item, spider):
        """Run the store_db method to store the item in the database."""
        self.store_db(item)
        return item

    def store_db(self, item):
        """Write the categories and links to the database."""
        self.cursor.execute(
            """INSERT INTO categories (category, url) VALUES (?, ?)""",
            (item["category"], item["url"]),
        )
        self.conn.commit()


# class SeenUrlsPipeline:
#     def __init__(self):
#         self.seen_urls = set()

#     def process_item(self, item, spider):
#         if item["url"] in self.seen_urls:
#             raise DropItem(f"Duplicate item found: {item!r}")
#         else:
#             self.seen_urls.add(item["url"])
#             return item
