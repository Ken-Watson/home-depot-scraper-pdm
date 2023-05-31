"""
This module provides a web application built with Streamlit that enables
the user to select a product category, fetch product data from a SQLite
database, and display the product data in both table format and as a
JSON API endpoint.

The web application assumes that a separate Scrapy project periodically
scrapes product data from various categories and stores the data in an
SQLite database. The table names in the SQLite database should correspond
to the product categories.

Functions:
main() - The main function of the Streamlit application. It provides
a user interface for the user to select a product category, fetch the
product data, and display the data.

get_products_from_db(category: str) - Function to fetch product data
from the SQLite database. It takes a product category as input and returns
a list of dictionaries where each dictionary contains the product data.

Modules used:
streamlit - Used to build the web application.
json - Used to convert the product data to JSON format.
sqlalchemy - Used to connect to the SQLite database and fetch data.
"""

import os

import streamlit as st
from dotenv import load_dotenv
from sqlalchemy import MetaData, Table, create_engine, select

load_dotenv()

def get_database_url():
    """Function to get the database URL from the environment variables."""
    url = os.getenv("DB_URL")
    if not url:
        raise ValueError("DATABASE_URL environment variable not found. Please set it in your .env file.")
    return url

# Create a database connection
db_url = get_database_url()
engine = create_engine(db_url)

print(db_url)
print("Current working directory:", os.getcwd())

# Create a table object
def get_categories_from_db():
    """
    Function to fetch product data from the SQLite database. It takes a
    product category as input and returns a list of dictionaries where
    each dictionary contains the product data.
    """

    with engine.connect() as conn:
        meta = MetaData(bind=engine)
        categories = Table("categories", meta, autoload=True, autoload_with=engine)
        query = select(categories.c.category)
        result = conn.execute(query).fetchall()

        # Convert the result to a list of dictionaries
        categories = [category[0] for category in result]
        print(categories)

        return categories

def get_selected_category_from_db(selected_category):
    """
    Function to fetch product data from the SQLite database. It takes a
    product category as input and returns a list of dictionaries where
    each dictionary contains the product data.
    """
    with engine.connect() as conn:
        meta = MetaData(bind=engine)
        categories = Table("categories", meta, autoload=True, autoload_with=engine)
        query = select(categories.c.category).where(categories.c.category == selected_category)
        result = conn.execute(query).fetchall()

        # Convert the result to a list of dictionaries
        selected_category = [category[0] for category in result]

        return selected_category

def main():
    """
    The main function of the Streamlit application. It provides a user
    interface for the user to select a product category, fetch the product
    data, and display the data.
    """
    st.title('Product Scraper')

    categories = get_categories_from_db()

    selected_category = st.selectbox('Choose a product category', categories)
    
    # Create a button for the user to start the scraping process
    if st.button('Fetch Products'):
        st.write(f'Fetching products in the {selected_category} category...')
        fetched_products = get_selected_category_from_db(selected_category)
        st.write(f'Found {len(fetched_products)} products.')

        # Display the fetched data in a table
        st.write(fetched_products)


if __name__ == '__main__':
    main()
