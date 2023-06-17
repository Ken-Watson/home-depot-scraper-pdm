import os
import subprocess

# Get the absolute path of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the relative path to the Streamlit app directory
app_directory = os.path.join(script_directory, "front_end")

if os.path.isdir(app_directory):
    subprocess.run(["streamlit", "run", "categories_streamlit.py"], check=True, cwd=app_directory)
else:
    print(f"Error: Invalid app directory path: {app_directory}")
