from database.base_database import BaseDatabase

def test_connection():
    """Test the connection to the database."""
    database = BaseDatabase("hdscraper/categories.db")
    if database.conn:
        print("Connection successful!")
    else:
        print("Connection failed!")

if __name__ == "__main__":
    test_connection()
    