# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import sqlite3
from typing import Optional

from database.category_database import CategoryDatabase
from database.product_detail_database import ProductDetailDatabase
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class CategoryDatabasePipeline:
    """Pipeline to handle the categories table."""
    def __init__(self):
        self.database: Optional[CategoryDatabase] = None

    def open_spider(self, spider):
        """Open the connection to the database."""
        self.database = CategoryDatabase("hdscraper.db")
        self.database.create_table()

    def close_spider(self, spider):
        """Close the connection to the database."""
        if self.database is not None:
            self.database.close()

    def process_item(self, item, spider):
        """Write the categories and links to the database."""
        if item.get("category") and item.get("url"):
            if self.database is not None:
                self.database.write_data(item)
            return item
        else:
            raise DropItem(f"Missing category or url in {item}")

class CategoryDatabasePipeline:
    """Pipeline to handle the categories table."""
    def __init__(self):
        self.database: Optional[ProductDetailDatabase] = None

    def open_spider(self, spider):
        """Open the connection to the database."""
        self.database = ProductDetailDatabase("hdscraper.db")
        self.database.create_table()

    def close_spider(self, spider):
        """Close the connection to the database."""
        if self.database is not None:
            self.database.close()

    def process_item(self, item, spider):
        """Write the categories and links to the database."""
        if item.get("category") and item.get("url"):
            if self.database is not None:
                self.database.write_data(item)
            return item
        else:
            raise DropItem(f"Missing category or url in {item}")