import tkinter as tk
from src.app.ingredientsMenu import IngredientsMenu


class Sidebar(tk.Frame):

    def __init__(self, parent, helper):
        super().__init__(parent, bg = 'Red', padx = 10, pady = 10)

        but1 = tk.Button(self, text='cum')
        but2 = tk.Button(self, text='cum')
        but3 = tk.Button(self, text='cum1')

        self.pack(fill='both', expand=True)
        but1.pack(side=tk.TOP)
        but2.pack(side=tk.BOTTOM)
        but3.pack(side=tk.TOP)

        IngredientsMenu(helper)