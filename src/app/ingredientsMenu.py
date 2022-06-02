
import tkinter as tk
from tkinter import ttk

from src.database.database import Ingredients

from src.app.colors import COLORS

class IngredientsMenu(tk.Frame):

    def select(table:ttk.Treeview, ing:tk.Entry)-> None:
        ing.delete(0, tk.END)
        item = table.item(table.selection()[0])['values'][0]
        ing.insert(0, item)

    def add(table:ttk.Treeview, ing:tk.Entry, unit:tk.Entry, ppu:tk.Entry)->None:
        Ingredients.add(ing.get(), unit.get(), float(ppu.get()))
        table.insert('', tk.END, values = (
                ing.get(),
                unit.get(),
                ppu.get()))
        ing.delete(0,tk.END)
        unit.delete(0,tk.END)
        ppu.delete(0,tk.END)

    def save(table:ttk.Treeview, ing:tk.Entry, unit:tk.Entry, ppu:tk.Entry)->None:
        selected_item = table.selection()[0]
        Ingredients.u(ing.get(), float(ppu.get()))
        table.set(selected_item, 2, float(ppu.get()))
        ing.delete(0,tk.END)
        unit.delete(0,tk.END)
        ppu.delete(0,tk.END)

    def rm(table:ttk.Treeview, ing:tk.Entry)->None:
        selected_item = table.selection()[0]
        Ingredients.rm(ing.get())
        table.delete(selected_item)
        ing.delete(0,tk.END)

    def __init__(self, parent):
        super().__init__(parent)

        #### CONTAINERS ####
        tableContainer = tk.Frame(self, height='600', width='700')

        container = tk.Frame(self, height='600', width='300', bg=COLORS.B03, padx=10, pady=10)

        newBoxesContainer = tk.Frame(container,
            bg=COLORS.B02, 
            highlightbackground=COLORS.BLUE,
            highlightthickness=3
        )
        editBoxesContainer = tk.Frame(container,
            bg=COLORS.B02, 
            highlightbackground=COLORS.MAGENTA,
            highlightthickness=3
        )


        #### OTHER ELEMENTS ####
        newLabel = tk.Label(container, text='New',
            bg=COLORS.B03,
            fg=COLORS.BLUE,
        )
        editLabel = tk.Label(container, text='Edit',
            bg=COLORS.B03,
            fg=COLORS.MAGENTA,
        )

        newIngEntry = tk.Entry(newBoxesContainer,
            font=('TkDefaultFont 12'),
            bg=COLORS.B02,
            fg=COLORS.B2
        )
        newUnitEntry = tk.Entry(newBoxesContainer,
            font=('TkDefaultFont 12'),
            bg=COLORS.B02,
            fg=COLORS.B2
        )
        newPpuEntry = tk.Entry(newBoxesContainer,
            font=('TkDefaultFont 12'),
            bg=COLORS.B02,
            fg=COLORS.B2
        )
        addButton = tk.Button(newBoxesContainer, text='Add',
            bg=COLORS.B02,
            activebackground=COLORS.B01,
            fg=COLORS.B2,
            command=lambda:IngredientsMenu.add(
                table,
                newIngEntry,
                newUnitEntry,
                newPpuEntry
                
            )
        )

        editIngEntry = tk.Entry(editBoxesContainer,
            font=('TkDefaultFont 12'),
            bg=COLORS.B02,
            fg=COLORS.B2
        )
        editUnitEntry = tk.Entry(editBoxesContainer,
            font=('TkDefaultFont 12'),
            bg=COLORS.B02,
            fg=COLORS.B2
        )
        editPpuEntry = tk.Entry(editBoxesContainer,
            bg=COLORS.B02,
            fg=COLORS.B2,
            font=('TkDefaultFont 12')
        )
        saveButton = tk.Button(editBoxesContainer, text='Save',
            bg=COLORS.B02,
            activebackground=COLORS.B01,
            fg=COLORS.B2, 
            command=lambda:IngredientsMenu.save(
                table,
                editIngEntry,
                editUnitEntry,
                editPpuEntry
                
            )
        )
        rmButton = tk.Button(editBoxesContainer, text='Delete',
            bg=COLORS.B02,
            activebackground=COLORS.B01,
            fg=COLORS.B2,
            command=lambda:IngredientsMenu.rm(
                table,
                editIngEntry
            ))

        #### TABLE ELEMENTS ####
        table = ttk.Treeview(tableContainer,
        padding=[10, 10], 
        columns=('ingredient', 'unit', 'price per unit'),
        show='headings',
        selectmode='browse')

        table.heading('ingredient', text='ingredient')
        table.heading('unit', text='unit')
        table.heading('price per unit', text='price per unit')

        for ing in Ingredients.q_all():
            table.insert('', tk.END, values = (
                ing['ingredient'],
                ing['unit'],
                ing['price_per_unit']))

        #### PACKING ####
        
        container.pack(side=tk.RIGHT, fill = 'both', expand=False)
        tableContainer.pack(fill = 'both', expand=True)

        table.pack(fill='both', expand = True, side=tk.TOP)
        table.bind('<Double-1>', lambda x:IngredientsMenu.select(table, editIngEntry))

        newLabel.pack(side=tk.TOP, anchor='w')
        newBoxesContainer.pack(side=tk.TOP, anchor='w')
        newIngEntry.pack()
        newUnitEntry.pack()
        newPpuEntry.pack()
        addButton.pack(side=tk.BOTTOM, anchor='w')

        editLabel.pack(side=tk.TOP, anchor='w')
        editBoxesContainer.pack(side=tk.TOP, anchor='w')
        editIngEntry.pack()
        editUnitEntry.pack()
        editPpuEntry.pack()
        saveButton.pack(side=tk.BOTTOM, anchor='w')
        rmButton.pack(side=tk.BOTTOM, anchor='w')

