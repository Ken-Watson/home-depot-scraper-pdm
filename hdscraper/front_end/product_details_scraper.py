import time
import concurrent.futures
from pprint import pprint
from typing import List

from product_details.api_session import ApiSession

API_URL = "https://www.homedepot.com/federation-gateway/graphql?opname=searchModel"


class ProductDetailsScraper:
    """Class to scrape product details from a category page on HomeDepot.com"""

    def __init__(self, category_url: str, api_session: ApiSession):
        self.category_url = category_url
        self.api_session = api_session
        self.all_products = []

    def get_category_code(self, url):
        """Return the category code from the category URL"""
        return url.split("N-")[-1].split("?catStyle")[0]

    def scrape_product_data(self, product: dict) -> List[dict]:
        """Extract relevant data from a product"""
        info = product.get("info", {})
        identifiers = product.get("identifiers", {})
        pricing = product.get("pricing", {})
        key_product_features_items = product.get("keyProductFeatures")

        if key_product_features_items and key_product_features_items != "null":
            key_product_features_items = key_product_features_items.get(
                "keyProductFeaturesItems", []
            )
        else:
            key_product_features_items = []

        if key_product_features_items:
            key_product_features = key_product_features_items[0]
            features = key_product_features.get("features", [])
        else:
            features = []

        # create a list of features
        features_list = [
            {"name": feature.get("name"), "value": feature.get("value")}
            for feature in features
        ]

        product_data = {
            "category": info.get("categoryHierarchy", "Unknown"),
            "brand_name": identifiers.get("brandName", "Unknown"),
            "item_id": identifiers.get("itemId", "Unknown"),
            "model_number": identifiers.get("modelNumber", "Unknown"),
            "product_description": identifiers.get("productLabel", "Unknown"),
            "price": pricing.get("value", "Unknown"),
            "features": features_list,
            "product_url": f"https://www.homedepot.com/{identifiers.get('canonicalUrl')}",
        }

        return [product_data]

    def start_process(self):
        """Retrieve and process product data for a given category"""

        # An index is required for the page size and offset.
        index = 0

        # Category code is used in the API request
        category_code = self.get_category_code(self.category_url)

        total_products = None

        with concurrent.futures.ThreadPoolExecutor() as executor:
            while total_products is None or index < total_products:
                futures = []
                for _ in range(4):  # Adjust the number of concurrent requests as per your needs
                    future = executor.submit(self.get_product_page, index, category_code)
                    futures.append(future)
                    index += 24

                for future in concurrent.futures.as_completed(futures):
                    results, total_products = future.result()
                    self.all_products.extend(results)

                print(f"Scraped {len(self.all_products)} products")

                time.sleep(4)  # Introduce delay between batches of requests

        return self.all_products

    def get_product_page(self, index, category_code):
        """Scrape and process product data for a given page"""
        api_session = self.api_session(f"{self.category_url}{str(index)}")
        response = api_session.make_api_request(API_URL, index, category_code)
        if response:
            data = response.get("data", {}).get("searchModel", {})
            total_products = data.get("searchReport", {}).get("totalProducts", 0)
            products = data.get("products", [])

            product_data = []
            for product in products:
                product_data.extend(self.scrape_product_data(product))

            return product_data, total_products


# if __name__ == "__main__":
#     # pylint: disable=C0301
#     CATEGORY_URL = "https://www.homedepot.com/b/Cleaning-Household-Essentials-Room-Fresheners-Air-Fresheners/N-5yc1vZcb2j?catStyle=ShowProducts&Nao="

#     get_product_data = ProductDetailsScraper(CATEGORY_URL, ApiSession)
#     product_list = get_product_data.start_process()

#     for item in product_list:
#         pprint(item)
#         print("------------------------")
