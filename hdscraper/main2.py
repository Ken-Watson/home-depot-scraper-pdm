# import os
# import subprocess

import threading
import uvicorn

from .front_end.categories_streamlit import app as fetch_products_app
from .front_end.categories_streamlit import fetch_products

# # Get the absolute path of the current script
# script_directory = os.path.dirname(os.path.abspath(__file__))

# # Specify the relative path to the Streamlit app directory
# app_directory = os.path.join(script_directory, "front_end")

# if os.path.isdir(app_directory):
#     subprocess.run(["streamlit", "run", "categories_streamlit.py"], check=True, cwd=app_directory)
# else:
#     print(f"Error: Invalid app directory path: {app_directory}")

# Start the Streamlit app in a separate thread
def start_streamlit_app():
    fetch_products()

# if __name__ == '__main__':
#     streamlit_thread = threading.Thread(target=start_streamlit_app)
#     streamlit_thread.start()

#     # Start the FastAPI app using Uvicorn
#     uvicorn.run(fetch_products_app, host="0.0.0.0", port=8000)
