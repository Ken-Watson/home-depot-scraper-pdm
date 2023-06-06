# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
from typing import Optional

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from dotenv import load_dotenv

from database.category_database import CategoryDatabase
from hdscraper.items import HdscraperCategoryItem

load_dotenv()


class CategoryDatabasePipeline:
    """Pipeline to handle the categories table."""
    def __init__(self):
        self.database: Optional[CategoryDatabase] = None

    def open_spider(self, spider):
        """Open the connection to the database."""
        url = os.getenv("DB_URL")
        self.database = CategoryDatabase(url)
        self.database.create_table()

    def close_spider(self, spider):
        """Close the connection to the database."""
        if self.database is not None:
            self.database.close()

    def process_item(self, data, spider):
        """Write the categories and links to the database."""
        adapter = ItemAdapter(data)
        category = adapter.get("category")
        url = adapter.get("url")
        if category and url:
            if self.database is not None:
                self.database.write_data(data)
            return data
        raise DropItem(f"Missing category or url in {data}")

# class ProductDetailDatabasePipeline:
#     """Pipeline to handle the categories table."""
#     def __init__(self):
#         self.database: Optional[ProductDetailDatabase] = None

#     def open_spider(self, spider):
#         """Open the connection to the database."""
#         self.database = ProductDetailDatabase("product_details.db")
#         self.database.create_table()

#     def close_spider(self, spider):
#         """Close the connection to the database."""
#         if self.database is not None:
#             self.database.close()

#     def process_item(self, data, spider):
#         """Write the product details to the database."""
#         required_fields = ["category_id", "brand_name", "item_id", "model_number", "product_description", "price", "product_url"]
#         if all(field in data for field in required_fields):
#             if self.database is not None:
#                 self.database.write_data(data)
#             return data
#         raise DropItem(f"Missing one or more required fields in {data}")
