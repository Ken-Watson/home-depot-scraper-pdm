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
import threading

import streamlit as st
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from sqlalchemy import MetaData, Table, create_engine, select

from hdscraper.product_details.product_details_scraper import (
    ApiSession, ProductDetailsScraper)

app = FastAPI()

load_dotenv()

def get_database_url():
    """Function to get the database URL from the environment variables."""
    url = os.getenv("DB_URL")
    if not url:
        raise ValueError("DB_URL environment variable not found. Please set it in your .env file.")
    return url

def get_categories_from_db(engine):
    """
    Function to fetch product categories from the SQLite database.
    It takes a database engine as input and returns a list of categories.
    """
    try:
        with engine.connect() as conn:
            meta = MetaData(bind=engine)
            categories_table = Table("categories", meta, autoload=True, autoload_with=engine)
            query = select(categories_table.c.category)
            result = conn.execute(query).fetchall()
            categories = [category[0] for category in result]
            return categories
    except Exception as exc:
        print(f"Error accessing the database: {str(exc)}")
        return []

def get_selected_category_urls_from_db(engine, selected_category):
    """
    Function to fetch product URLs for the selected category from the SQLite database.
    It takes a database engine and a selected category as input and returns a list of URLs.
    """
    try:
        with engine.connect() as conn:
            meta = MetaData(bind=engine)
            categories_table = Table("categories", meta, autoload=True, autoload_with=engine)
            query = select(categories_table.c.url).where(categories_table.c.category == selected_category)
            result = conn.execute(query).fetchall()
            urls = [row[0] for row in result]
            return urls
    except Exception as exc:
        print(f"Error accessing the database: {str(exc)}")
        return []



def fetch_products():
    """
    The main function of the Streamlit application.
    It provides a user interface for the user to select a product category,
    fetch the product data, and display the data.
    """
    st.title('Home Depot Product Scraper')
    st.write('This application enables you to fetch product data from the Home Depot website.')
    db_url = get_database_url()
    engine = create_engine(db_url)

    categories = get_categories_from_db(engine)

    selected_category = st.selectbox('Choose a product category', categories)

    # Create a button for the user to start the scraping process
    if st.button('Fetch Product Data'):
        fetched_products = get_selected_category_urls_from_db(engine, selected_category)

        for url in fetched_products:
            st.write(f'Scraping category for product data: {url}...')
            get_product_data = ProductDetailsScraper(url, ApiSession)
            products_returned = get_product_data.start_process()

            product_count = len(products_returned)
            st.write(f'Found {product_count} products.')

            st.json(products_returned, expanded=False)

        st.write('Finished scraping products.')

        # Add a stop button to gracefully exit the app
        if st.button('Close App'):
            st.stop()

# def run_fastapi():
#     uvicorn.run(app, host="0.0.0.0", port=8000)

# def run_streamlit():
#     fetch_products()

if __name__ == '__main__':
    # fastapi_thread = threading.Thread(target=run_fastapi)
    # streamlit_thread = threading.Thread(target=run_streamlit)

    # fastapi_thread.start()
    # streamlit_thread.start()
    fetch_products()
