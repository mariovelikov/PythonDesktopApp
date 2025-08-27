import tkinter as tk
from tkinter import ttk
from table import Table

class SearchByType:
    __path = "items.txt"
    columns = ("Stock Code", "Title", "Type", "Autor", "Price", "Quantity")

    def __init__(self, root):
        super().__init__()
        self.__data = None
        self.__window = tk.Toplevel(root)
        self.__window.title("Search by Type")
        self.__window.geometry("500x500")

        self.__options:dict = dict()

        self.__get_all_types()

        cb_selected = tk.StringVar()
        self.__cb = ttk.Combobox(self.__window, values=list(self.__options.keys()), state="readonly",  textvariable=cb_selected)
        self.__cb.set("Select a type!")
        self.__cb.pack()
        self.__cb.bind("<<ComboboxSelected>>", self.get_selected)

        self.tb = Table(self.__window, self.columns, [])

        self.__window.mainloop()

    def __del__(self):
        print("Search bar deleted")

    def get_selected(self, event)-> None:
        self.tb.load_new_data(self.__window, self.columns, self.__options.get(self.__cb.get()))

    def __get_all_types(self)->None:
        with open(self.__path, "r", encoding="utf-8") as file:
            self.__data = file.readlines()
            file.close()

        for item in self.__data:
            key:str = item.strip().split(",")[2]

            if key in self.__options.keys():
                self.__options[item.strip().split(",")[2]].append(item)
            else:
                self.__options[item.strip().split(",")[2]] = [item]