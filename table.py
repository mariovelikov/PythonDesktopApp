import tkinter as tk
from tkinter import ttk

class Table:
    def __init__(self, root, columns, data:list):
        self.root = root
        self.columns = columns
        self.data:list = data
        self.table = ttk.Treeview(self.root, columns=self.columns, show="headings")
        self.display()

    def load_new_data(self, root, columns, data:list):
        self.root = root
        self.columns = columns
        self.data: list = data
        self.display()

    def display(self):
        self.delete_rows()
        for col in self.columns:
            self.table.heading(col, text=col)

        for line in self.data:
            self.table.insert("", tk.END, values=line.strip().split(","))
        self.table.pack(expand=True, fill="both")

    def delete_rows(self):
        for row in self.table.get_children():
            self.table.delete(row)
