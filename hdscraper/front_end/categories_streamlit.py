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

import json
import os

import streamlit as st
from dotenv import load_dotenv
from sqlalchemy import MetaData, Table, create_engine, select

# Load the .env file
load_dotenv()

def get_database_url():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise Exception("DATABASE_URL environment variable not found. Please set it in your .env file.")
    return db_url

# Create a database connection
database_url = get_database_url()
print(database_url)
print("Current working directory:", os.getcwd())

engine = create_engine(database_url)
meta = MetaData(bind=engine)

# Create a table object
def get_categories_from_db():
    """
    Function to fetch product data from the SQLite database. It takes a
    product category as input and returns a list of dictionaries where
    each dictionary contains the product data.
    """
    categories = Table("categories", meta, autoload=True, autoload_with=engine)

    # Create a select query
    query = select(categories.c.category)
    conn = engine.connect()
    result = conn.execute(query).fetchall()

    # Convert the result to a list of dictionaries
    categories = [category[0] for category in result]

    return categories

def get_selected_category_from_db(selected_category):
    """
    Function to fetch product data from the SQLite database. It takes a
    product category as input and returns a list of dictionaries where
    each dictionary contains the product data.
    """
    categories = Table("categories", meta, autoload=True, autoload_with=engine)

    # Create a select query
    query = select(categories.c.category).where(categories.c.category == selected_category)
    conn = engine.connect()
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

    # List the available product categories
    # categories = ['electronics', 'clothing', 'home', 'toys']

    categories = get_categories_from_db()

    selected_category = st.selectbox('Choose a product category', categories)

    # Create a button for the user to start the scraping process
    if st.button('Fetch Products'):
        st.write(f'Fetching products in the {selected_category} category...')
        fetched_products = get_selected_category_from_db(selected_category)
        st.write(f'Found {len(fetched_products)} products.')

        # # Display the fetched data in a table
        # st.write(fetched_products)

        # # Create a JSON API endpoint with the fetched data
        # json_data = json.dumps(fetched_products)
        # st.text_area('JSON API Endpoint:', value=json_data, height=200)

if __name__ == '__main__':
    main()
