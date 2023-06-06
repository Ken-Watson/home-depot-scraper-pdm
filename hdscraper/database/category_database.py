"""This module is used to handle operations for the categories table."""


from .base_database import BaseDatabase


class CategoryDatabase(BaseDatabase):
    """This class is used to handle operations for the categories table."""

    def create_table(self):
        """Create the category table"""
        self.cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY,
        category TEXT,
        url TEXT
        )
        """
        )
        self.conn.commit()

    def write_data(self, data):
        """Write the categories and links to the database."""
        category_title = data["category"].title() # Capitalize each word
        self.cursor.execute(
            """INSERT INTO categories (category, url) VALUES (?, ?)""",
            (category_title, data["url"]),
        )
        self.conn.commit()

    def close(self):
        """Close the connection to the database."""
        self.cursor.close()
        self.conn.close()
