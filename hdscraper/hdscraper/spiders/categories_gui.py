"""This module provides a GUI interface for a web scraper that extracts product data
from Home Depot's website. The user selects one or more categories to scrape, and the
scraper, implemented using Scrapy, stores the scraped data in an SQLite database. The
get_categories function retrieves the available categories from the database. The module
uses tkinter to create the GUI interface.
"""
import sqlite3
import tkinter as tk
from tkinter import ttk


def on_button_click():
    categories = []
    for i in range(len(category_vars)):
        if category_vars[i].get() == 1:
            categories.append(categories_list[i])
    start_scrapy(categories)


def get_categories():
    """Get categories from database"""
    open_db = sqlite3.connect("hdscraper.db")
    cursor = open_db.cursor()
    categories = cursor.execute("SELECT category FROM categories")
    categories = [category[0] for category in categories]

    # Sort the categories alphabetically
    categories.sort()

    return categories


def gui():
    """Create GUI"""
    root = tk.Tk()
    root.title("Home Depot Scraper")

    categories_list = get_categories()

    # Create a list of integers that correspond to the categories starting with 0
    category_vars = [tk.IntVar(value=0) for _ in range(len(categories_list))]

    # Create a canvas to hold the Checkbutton widgets
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar to the canvas
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas to use the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # Create a frame to hold the Checkbutton widgets
    frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Create a grid of Checkbutton widgets
    rows = (len(categories_list) - 1) // 5 + 1
    cols = 5
    for i in range(rows):
        for j in range(cols):
            index = i * cols + j
            if index < len(categories_list):
                tk.Checkbutton(
                    frame, text=categories_list[index], variable=category_vars[index]
                ).grid(row=i, column=j, sticky="w")

    # Set the width of each column to be the same
    for i in range(cols):
        frame.grid_columnconfigure(i, minsize=200)

    # Calculate the width of the window based on the number of columns
    width = cols * 200 + 50

    tk.Button(root, text="Scrape", command=on_button_click).pack()

    root.geometry(f"{width}x500")
    root.mainloop()


if __name__ == "__main__":
    gui()
