# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import sqlite3

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class HdscraperPipeline:
    def __init__(self, db_name):
        self.db_connection(db_name)
        self.create_table()

    def db_connection(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS categories ("
            "id INTEGER PRIMARY KEY,"
            "category TEXT,"
            "url TEXT,"
            ")"
        )
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.cursor.execute(
            """INSERT INTO categories (category, url) VALUES (?, ?)""",
            (item["category"], item["url"]),
        )
        self.conn.commit()
