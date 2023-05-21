"""This module is used to handle operations for the product details table."""

from base_database import BaseDatabase

class ProductDetailDatabase(BaseDatabase):
    """This class is used to handle operations for the product details table."""

    def create_table(self):
        """Create the product details table"""
        # Implement the SQL query to create the product details table.
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS product_details (
                id INTEGER PRIMARY KEY,
                category_id INTEGER,
                brand_name TEXT,
                item_id TEXT,
                model_number TEXT,
                product_description TEXT,
                price FLOAT,
                product_url TEXT,
                FOREIGN KEY(category_id) REFERENCES categories(id)
            )
            """
        )
        self.conn.commit()

    def write_data(self, data):
        """Write the product details to the database."""
        # Implement the SQL query to insert product details.
        self.cursor.execute(
            """
            INSERT INTO product_details 
            (category_id, brand_name, item_id, model_number, product_description, price, product_url) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                data["category_id"],
                data["brand_name"],
                data["item_id"],
                data["model_number"],
                data["product_description"],
                data["price"],
                data["product_url"],
            ),
        )
        self.conn.commit()

    def close(self):
        """Close the connection to the database."""
        self.cursor.close()
        self.conn.close()