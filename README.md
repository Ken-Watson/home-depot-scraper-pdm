# HomeDepot.com Product Scraper Project

## Introduction:
The aim of this project is to build a web scraper in Python using a combination of tools to extract product data from HomeDepot.com. The web scraper will have an online interface using Streamlit where the user can select multiple categories they want to query. The selected categories will be used to create a list of category links which will be fed into a product details scraper. The spider will read each link, scrape all the product data, and return the data back to the user through an API.

## Technologies Used:
  * Python 3
  * Scrapy
  * SQLite
  * SQLAlchemy
  * Streamlit
  * FastAPI

## Project Structure:
The project will consist of two web scraper files:

  * categories_spider.py: This spider built using Scrapy will extract all the category links and category names from the Home Depot website. It will then store this information in a database.
  * product_details_scraper.py: The Product Detail Scraper is a script that utilizes the category links stored in the database. It makes URL requests to extract detailed information about products, including their name, price, and description. The scraper is designed to fetch the relevant data from the web pages corresponding to the category links stored in the database.

## Database Schema:
The database will consist of two tables:

  * categories: This table will store the category name and category link for each category.
  * product_details: This table will store the product details such as product name, description, dimensions, price, rating, etc.

## Web Interface:
The web interface built with Streamlit will allow the user to select multiple categories they want to query. Once the user has made their selection, they will click a button which will trigger the scraping process.

Run it from the project root directory like this:

```
streamlit run hdscraper/front_end/categories_streamlit.py
```

## Scraping Process:
1. The CategoryCrawler spider will be executed. It will extract all the category links and category names from the Home Depot website.
2. The extracted category links and category names will be stored in the database.
3. The user will select multiple categories they want to query in the online interface.
4. The selected categories will be used to create a list of category links which will be read and parsed in the product details scraper file.
5. The product details scraper will be executed. It will use the category links stored in the database to extract product details such as name, price, and description.
6. The extracted product details will be returned to the user and accessible through an API.

