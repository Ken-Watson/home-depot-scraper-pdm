from fastapi import FastAPI

app = FastAPI()

@app.get("/api/products")
def get_products(fetch_products: callable):
    fetched_products = fetch_products()  # Fetch your JSON data
    return fetched_products