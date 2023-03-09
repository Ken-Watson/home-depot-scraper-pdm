# HomeDepot.com Product Scraper Project

## Introduction:
The aim of this project is to build a web scraper in Python using Scrapy. The web scraper will have a Graphical User Interface (GUI) where the user can select multiple categories they want to query. The selected categories will be used to create a list of category links which will be fed into a product details spider. The spider will read each link, scrape all the product data, and store it in a SQLite database.

## Technologies Used:
  * Python 3
  * Scrapy
  * SQLite
  
## Project Structure:
The project will consist of two spiders:

  * CategoryCrawler: This spider will extract all the category links and category names from the Home Depot website. It will then store this information in a database.
  * ProductDetailsSpider: This spider will use the category links stored in the database to extract product details such as name, price, and description.
  
## Database Schema:
The database will consist of a single table:

  * categories: This table will store the category name and category link for each category.
  * product_details: This table will store the product details such as product name, description, dimensions, price, rating, etc.
  
## GUI:
The GUI will allow the user to select multiple categories they want to query. Once the user has made their selection, they will click a button which will trigger the scraping process.

## Scraping Process:
1. The CategoryCrawler spider will be executed. It will extract all the category links and category names from the Home Depot website.
2. The extracted category links and category names will be stored in the database.
3. The user will select multiple categories they want to query in the GUI.
4. The selected categories will be used to create a list of category links which will be fed into the ProductDetailsSpider.
5. The ProductDetailsSpider will be executed. It will use the category links stored in the database to extract product details such as name, price, and description.
6. The extracted product details will be stored in the database.

## Conclusion:
In this project, a web scraper using Scrapy was built with a GUI to allow the user to select multiple categories they want to query. The extracted product details were stored in a SQLite database. This project can be extended to include more features such as image extraction and data visualization.
