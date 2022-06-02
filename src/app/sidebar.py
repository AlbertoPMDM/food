from ast import Lambda
import tkinter as tk
from src.app.ingredientsMenu import IngredientsMenu
from src.app.foodsMenu import FoodsMenu
from src.app.listWindow import ListWindow

from src.app.colors import COLORS


class Sidebar(tk.Frame):

    def show_foods(ingm:IngredientsMenu, foodm:FoodsMenu)-> None:
        ingm.pack_forget()
        foodm.pack(fill='both', expand=True)

    def show_ings(ingm:IngredientsMenu, foodm:FoodsMenu)-> None:
        foodm.pack_forget()
        ingm.pack(fill='both', expand=True)
        
        

    def __init__(self, parent, helper):
        super().__init__(parent, bg = COLORS.B03, padx = 10, pady = 10)

        ingm = IngredientsMenu(helper)
        foodm = FoodsMenu(helper)

        ingredientsButton = tk.Button(self, text='Ingredients', 
            pady=10,
            bg=COLORS.B02,
            activebackground=COLORS.B01,
            fg=COLORS.B2,
            command=lambda:Sidebar.show_ings(ingm, foodm)
        )
        foodsButton = tk.Button(self, text='Foods', 
            pady=10,
            bg=COLORS.B02,
            activebackground=COLORS.B01,
            fg=COLORS.B2,
            command=lambda:Sidebar.show_foods(ingm, foodm)
        )
        listButton = tk.Button(self, text='List', 
            pady=10,
            bg=COLORS.B02,
            activebackground=COLORS.B01,
            fg=COLORS.B2,
            command=lambda:ListWindow(self)
        )
        exitButton = tk.Button(self, text='Exit',
            pady=10,
            bg=COLORS.B02,
            activebackground=COLORS.B01,
            fg=COLORS.B2
        )

        self.pack(fill='both', expand=True)
        ingredientsButton.pack(side=tk.TOP, fill='x')
        foodsButton.pack(side=tk.TOP, fill='x')
        listButton.pack(side=tk.TOP, fill='x')
        exitButton.pack(side=tk.BOTTOM, fill='x')



        
        