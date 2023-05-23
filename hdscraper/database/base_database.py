"""
This module contains the DatabaseWriter class.
"""

import sqlite3
from abc import ABC, abstractmethod

class BaseDatabase(ABC):
    """This class is used to handle the base operations for a database."""

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    @abstractmethod
    def create_table(self):
        """Create the table if it doesn't exist."""

    @abstractmethod
    def write_data(self, data):
        """Write the data to the database."""

    def close(self):
        """Close the connection to the database."""
        self.cursor.close()
        self.conn.close()
