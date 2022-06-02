
import tkinter as tk
from tkinter import ttk

from src.database.database import Foods
from src.app.ingredientsWindow import IngredientsWindow

from src.app.colors import COLORS

class FoodsMenu(tk.Frame):

    def select(table:ttk.Treeview, food:tk.Entry)-> None:
        food.delete(0, tk.END)
        item = table.item(table.selection()[0])['values'][0]
        food.insert(0, item)

    def add(table:ttk.Treeview, food:tk.Entry, serv:tk.Entry)->None:
        Foods.add(food.get(), int(serv.get()))
        table.insert('', tk.END, values = (
                food.get(),
                int(serv.get()),
            )
        )
        food.delete(0,tk.END)
        serv.delete(0,tk.END)

    def save(table:ttk.Treeview, food:tk.Entry, serv:tk.Entry)->None:
        selected_item = table.selection()[0]
        Foods.u(food.get(), int(serv.get()))
        table.set(selected_item, 1, int(serv.get()))
        food.delete(0,tk.END)
        serv.delete(0,tk.END)

    def rm(table:ttk.Treeview, food:tk.Entry)->None:
        selected_item = table.selection()[0]
        Foods.rm(food.get())
        table.delete(selected_item)
        food.delete(0,tk.END)

    def __init__(self, parent):
        super().__init__(parent)

        #### CONTAINERS ####
        tableContainer = tk.Frame(self, height='600', width='700')

        container = tk.Frame(self, height='600', width='300', bg=COLORS.B03, padx=10, pady=10)

        newBoxesContainer = tk.Frame(container,
            bg=COLORS.B02, 
            highlightbackground=COLORS.ORANGE,
            highlightthickness=3
        )
        editBoxesContainer = tk.Frame(container,
            bg=COLORS.B02, 
            highlightbackground=COLORS.CYAN,
            highlightthickness=3
        )


        #### OTHER ELEMENTS ####
        newLabel = tk.Label(container, text='New',
            bg=COLORS.B03,
            fg=COLORS.ORANGE,
        )
        editLabel = tk.Label(container, text='Edit',
            bg=COLORS.B03,
            fg=COLORS.CYAN,
        )

        newFoodEntry = tk.Entry(newBoxesContainer,
            font=('TkDefaultFont 12'),
            bg=COLORS.B02,
            fg=COLORS.B2
        )
        newServEntry = tk.Entry(newBoxesContainer,
            font=('TkDefaultFont 12'),
            bg=COLORS.B02,
            fg=COLORS.B2
        )
        addButton = tk.Button(newBoxesContainer, text='Add',
            bg=COLORS.B02,
            activebackground=COLORS.B01,
            fg=COLORS.B2,
            command=lambda:FoodsMenu.add(
                table,
                newFoodEntry,
                newServEntry,
                
            )
        )

        editFoodEntry = tk.Entry(editBoxesContainer,
            font=('TkDefaultFont 12'),
            bg=COLORS.B02,
            fg=COLORS.B2
        )
        editServsEntry = tk.Entry(editBoxesContainer,
            font=('TkDefaultFont 12'),
            bg=COLORS.B02,
            fg=COLORS.B2
        )
        saveButton = tk.Button(editBoxesContainer, text='Save',
            bg=COLORS.B02,
            activebackground=COLORS.B01,
            fg=COLORS.B2,
            command=lambda:FoodsMenu.save(
                table,
                editFoodEntry,
                editServsEntry,
                
            )
        )
        rmButton = tk.Button(editBoxesContainer, text='Delete',
            bg=COLORS.B02,
            activebackground=COLORS.B01,
            fg=COLORS.B2,
            command=lambda:FoodsMenu.rm(
                table,
                editFoodEntry
            ))
        ingButton = tk.Button(editBoxesContainer, text='Ingredients',
            bg=COLORS.B02,
            activebackground=COLORS.B01,
            fg=COLORS.B2,
            command=lambda:IngredientsWindow(self, editFoodEntry.get())
        )

        #### TABLE ELEMENTS ####
        table = ttk.Treeview(tableContainer,
        padding=[10, 10], 
        columns=('food', 'servings'),
        show='headings',
        selectmode='browse')

        table.heading('food', text='food')
        table.heading('servings', text='servings')

        for food in Foods.q_all():
            table.insert('', tk.END, values = (
                food['food'],
                food['servings']
                )
            )

        #### PACKING ####
        container.pack(side=tk.RIGHT, fill = 'both', expand=False)
        tableContainer.pack(fill = 'both', expand=True)

        table.pack(fill='both', expand = True, side=tk.TOP)
        table.bind('<Double-1>', lambda x:FoodsMenu.select(table, editFoodEntry))

        newLabel.pack(side=tk.TOP, anchor='w')
        newBoxesContainer.pack(side=tk.TOP, anchor='w')
        newFoodEntry.pack()
        newServEntry.pack()
        addButton.pack(side=tk.BOTTOM, anchor='w')

        editLabel.pack(side=tk.TOP, anchor='w')
        editBoxesContainer.pack(side=tk.TOP, anchor='w')
        editFoodEntry.pack()
        editServsEntry.pack()
        saveButton.pack(side=tk.BOTTOM, anchor='w')
        rmButton.pack(side=tk.BOTTOM, anchor='w')
        ingButton.pack(side=tk.BOTTOM, anchor='w')

