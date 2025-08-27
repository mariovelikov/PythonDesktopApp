import tkinter as tk
import os

from table import Table
from search_by_type import SearchByType
from add_new_item import AddNewItem

class Bookstore:
    __data = []
    __path = "items.txt"
    window = tk.Tk()
    columns = ("Stock Code", "Title", "Type", "Autor", "Price", "Quantity")
    
    def __init__(self)->None:
        self.tb = None
        self.display()

    def display(self)->None:
        self.window.title("Books")
        self.window.geometry("500x250")

        # declare and show Buttons
        search_btn = tk.Button(self.window, text="Search by Type", command=self.search_by_type, cursor="hand2", anchor="center", font=("Arial", 12), justify="center", activebackground="white")
        add_item_btn = tk.Button(self.window, text="Add new item", command=self.add_new_item, cursor="hand2", anchor="center", font=("Arial", 12), activebackground="white")
        search_btn.pack(padx=10, pady=10)
        add_item_btn.pack(padx=10, pady=40)

        #load and show Table with data
        self.__get_data()
        self.tb = Table(self.window, self.columns, self.__data)
        self.window.mainloop()

    def __get_data(self)->None:
        if os.path.isfile(self.__path):
            with open(self.__path, "r", encoding="utf-8") as file:
                self.__data = file.readlines()
                file.close()
        else:
            f = open(self.__path, "x")
    
    def search_by_type(self)->None:
        window = SearchByType(self.window)

    def add_new_item(self):
        window = AddNewItem(self.window, self.tb, self.columns)

lb = Bookstore()
