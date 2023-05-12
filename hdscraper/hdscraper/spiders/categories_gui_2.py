"""This module provides a GUI interface for a web scraper that extracts product data
from Home Depot's website. The user selects one or more categories to scrape, and the
scraper, implemented using Scrapy, stores the scraped data in an SQLite database. The
get_categories function retrieves the available categories from the database. The module
uses tkinter to create the GUI interface.
"""
import sqlite3
import tkinter as tk
from tkinter import ttk
from product_details_spider import start_scrapy


class CategoryGUI:
    """Class for creating a GUI for selecting categories to scrape"""

    def __init__(self):
        self.categories = self.get_categories()
        self.category_vars = []
        self.category_links = []

    def button_clicked(self):
        """Start scrapy process when bun bbtton is clicked"""
        with sqlite3.connect(
            r"c:\Users\watso\OneDrive\DataProjects\Git Repos\home-depot-scraper-pdm\hdscraper\hdscraper\hdscraper.db"
        ) as conn:
            cursor = conn.cursor()
            for i, var in enumerate(self.category_vars):
                if var.get() == 1:
                    cursor.execute(
                        "SELECT url FROM categories WHERE category = ?",
                        (self.categories[i],),
                    )
                    self.category_links.append(cursor.fetchone()[0])
            conn.commit()

        start_scrapy(self.category_links)

    def get_categories(self):
        """Get categories from database"""
        with sqlite3.connect(
            r"c:\Users\watso\OneDrive\DataProjects\Git Repos\home-depot-scraper-pdm\hdscraper\hdscraper\hdscraper.db"
        ) as conn:
            cursor = conn.cursor()
            categories = cursor.execute("SELECT category FROM categories")
            self.categories = [category[0] for category in categories]
            # Sort the categories alphabetically
            self.categories.sort()
        return self.categories

    def gui(self):
        """Create GUI"""
        root = tk.Tk()
        root.title("Home Depot Scraper")

        # Create a list of integers that correspond to the categories starting with 0
        self.category_vars = [tk.IntVar(value=0) for _ in self.categories]

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
        rows = (len(self.categories) - 1) // 5 + 1
        cols = 5
        for i in range(rows):
            for j in range(cols):
                index = i * cols + j
                if index < len(self.categories):
                    tk.Checkbutton(
                        frame,
                        text=self.categories[index],
                        variable=self.category_vars[index],
                    ).grid(row=i, column=j, sticky="w")

        # Set the width of each column to be the same
        for i in range(cols):
            frame.grid_columnconfigure(i, minsize=200)

        # Calculate the width of the window based on the number of columns
        width = cols * 200 + 50

        # Create a button to start the scraping process
        tk.Button(
            root,
            text="Scrape",
            command=self.button_clicked,
        ).pack(side="bottom", pady=10)

        # Set the size of the window
        root.geometry(f"{width}x500")

        # Start the GUI
        root.mainloop()

    @classmethod
    def get_category_links(cls):
        """Return the category links selected by the user"""
        return cls().category_links


if __name__ == "__main__":
    start_gui = CategoryGUI()
    start_gui.gui()
