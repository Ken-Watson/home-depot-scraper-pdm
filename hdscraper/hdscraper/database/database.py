"""
This module contains the DatabaseWriter class.
"""

import sqlite3


class DatabaseWriter:
    """This class is used to write data to a database."""

    def __init__(self):
        self.conn = sqlite3.connect("hd_products.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS categories ("
            "id INTEGER PRIMARY KEY,"
            "category TEXT,"
            "url TEXT,"
            ")"
        )
        self.conn.commit()

    def write_category(self, category):
        """Write the categories and links to the database."""
        self.cursor.execute(
            """INSERT INTO categories (category, url) VALUES (?, ?)""",
            (category["category"], category["url"]),
        )
        self.conn.commit()

    def close(self):
        """Close the connection to the database."""
        self.cursor.close()
        self.conn.close()
