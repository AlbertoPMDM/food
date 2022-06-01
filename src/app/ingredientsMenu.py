
import tkinter as tk
from tkinter import ttk

from src.database.database import Ingredients

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
        super().__init__(parent, bg = 'Blue', padx=10, pady=10)

        #### CONTAINERS ####
        tableContainer = tk.Frame(self, height='600', width='700', bg='Pink', padx=10, pady=10 )

        container = tk.Frame(self, height='600', width='300', bg='Green', padx=10, pady=10)

        newBoxesContainer = tk.Frame(container, bg='Black', padx=10, pady=10)
        editBoxesContainer = tk.Frame(container, bg='Black', height='50', width='100', padx=10, pady=10)


        #### OTHER ELEMENTS ####
        newLabel = tk.Label(container, text='New')
        editLabel = tk.Label(container, text='Edit')

        newIngEntry = tk.Entry(newBoxesContainer)
        newUnitEntry = tk.Entry(newBoxesContainer)
        newPpuEntry = tk.Entry(newBoxesContainer)
        addButton = tk.Button(newBoxesContainer, text='Add',
            command=lambda:IngredientsMenu.add(
                table,
                newIngEntry,
                newUnitEntry,
                newPpuEntry
                
            )
        )

        editIngEntry = tk.Entry(editBoxesContainer)
        editUnitEntry = tk.Entry(editBoxesContainer)
        editPpuEntry = tk.Entry(editBoxesContainer)
        saveButton = tk.Button(editBoxesContainer, text='Save', 
            command=lambda:IngredientsMenu.save(
                table,
                editIngEntry,
                editUnitEntry,
                editPpuEntry
                
            )
        )
        rmButton = tk.Button(editBoxesContainer, text='Delete',
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
        self.pack(fill='both', expand=True)
        container.pack(side=tk.RIGHT, fill = 'both', expand=True)
        tableContainer.pack(fill = 'both', expand=True)

        table.pack(fill='both', expand = True, side=tk.TOP)
        table.bind('<Double-1>', lambda x:IngredientsMenu.select(table, editIngEntry))

        newLabel.pack()
        newBoxesContainer.pack()
        newIngEntry.pack(side=tk.TOP)
        newUnitEntry.pack(side=tk.TOP)
        newPpuEntry.pack(side=tk.TOP)
        addButton.pack(side=tk.LEFT)

        editLabel.pack()
        editBoxesContainer.pack()
        editIngEntry.pack(side=tk.TOP)
        editUnitEntry.pack(side=tk.TOP)
        editPpuEntry.pack(side=tk.TOP)
        saveButton.pack(side=tk.LEFT)
        rmButton.pack(side=tk.LEFT)

