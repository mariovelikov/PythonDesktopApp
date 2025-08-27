import tkinter as tk
from table import Table


class AddNewItem:
    def __init__(self, root, table:Table, columns:tuple=None):
        self.window = tk.Toplevel(root)
        self.tb = table
        self.columns = columns

        self.__titleL = tk.Label(self.window, text="Title")
        self.__title = tk.Entry(self.window, width=30)
        self.__typeL = tk.Label(self.window, text="Type ")
        self.__type = tk.Entry(self.window, width=30)
        self.__autorL = tk.Label(self.window, text="Autor")
        self.__autor = tk.Entry(self.window, width=30)
        self.__priceL = tk.Label(self.window, text="Price")
        self.__price = tk.Entry(self.window, width=30)
        self.__equityL = tk.Label(self.window, text="Quantity")
        self.__equity = tk.Entry(self.window, width=30)
        self.__titleL.pack()
        self.__title.pack(pady=5)
        self.__typeL.pack()
        self.__type.pack(pady=5)
        self.__autorL.pack()
        self.__autor.pack(pady=5)
        self.__priceL.pack()
        self.__price.pack(pady=5)
        self.__equityL.pack()
        self.__equity.pack(pady=5)

        self.__add_btn = tk.Button(self.window, text="Add Item", command=self.__add_item_and_reload_data, cursor="hand2", anchor="center", font=("Arial", 12), justify="center", activebackground="white")
        self.__add_btn.pack(pady=10, padx=10)
        self.__display()

    def __display(self):
        self.window.title("Books")
        self.window.geometry("500x350")

        self.window.mainloop()

    def __reload_data(self):
        with open("items.txt", "r", encoding="utf-8") as file:
            data = file.readlines()
            self.tb.load_new_data(self.window, self.columns, data)
            file.close()

    def __add_item_and_reload_data(self):
        title = self.__title.get()
        type_t = self.__type.get()
        autor = self.__autor.get()
        price = self.__price.get()
        equity = self.__equity.get()

        n = 0 # Get last number from line
        with open("items.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1]
                n = int(last_line.strip().split(",")[0]) + 1
                file.close()

        with open("items.txt", "a", encoding="utf-8") as file:
            new_line = f"{n}, {title}, {type_t}, {autor}, {price}, {equity}\n"
            file.write(new_line)
            file.close()

        self.__reload_data()
