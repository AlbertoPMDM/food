import tkinter as tk
from tkinter import ttk

from src.utils.utils import Utils
from src.database.database import Foods

from src.app.colors import COLORS

class IngredientsWindow(tk.Toplevel):

    
    '''
    {
        'arroz': {'ammount': 0.3, 'unit': 'kg', 'total': 11.1, 'price': 37.0}, 
        'lata de frijol': {'ammount': 1.0, 'unit': 'kg', 'total': 30.0, 'price': 30.0}
    }
    '''

    def select(table:ttk.Treeview, food:tk.Entry)-> None:
        food.delete(0, tk.END)
        item = table.item(table.selection()[0])['values'][0]
        food.insert(0, item)

    def add(table:ttk.Treeview, ing:tk.Entry, amt:tk.Entry, food:str)->None:
        Foods.addTo(float(amt.get()), ing.get(), food)
        table.insert('', tk.END, values = (
                ing.get(),
                float(amt.get()),
            )
        )
        ing.delete(0,tk.END)
        amt.delete(0,tk.END)

    def save(table:ttk.Treeview, ing:tk.Entry, amt:tk.Entry, food:str)->None:
        selected_item = table.selection()[0]
        Foods.uAmt(float(amt.get()), ing.get(), food)
        table.set(selected_item, 1, int(amt.get()))
        ing.delete(0,tk.END)
        amt.delete(0,tk.END)

    def rm(table:ttk.Treeview, ing:tk.Entry, food:str)->None:
        selected_item = table.selection()[0]
        Foods.rmFrom(ing.get(), food)
        table.delete(selected_item)
        ing.delete(0,tk.END)

    def __init__(self, parent, selected_food):
        super().__init__(parent)
        self.title("Ingredients")

        #### CONTAINERS ####
        tableContainer = tk.Frame(self, height='600', width='700' )

        container = tk.Frame(self, height='600', width='300', bg=COLORS.B03, padx=10, pady=10)

        newBoxesContainer = tk.Frame(container,
            bg=COLORS.B02, 
            highlightbackground=COLORS.GREEN,
            highlightthickness=3
        )
        editBoxesContainer = tk.Frame(container,
            bg=COLORS.B02, 
            highlightbackground=COLORS.VIOLET,
            highlightthickness=3
        )


        #### OTHER ELEMENTS ####
        newLabel = tk.Label(container, text='New',
            bg=COLORS.B03,
            fg=COLORS.GREEN,
        )
        editLabel = tk.Label(container, text='Edit',
            bg=COLORS.B03,
            fg=COLORS.VIOLET,
        )

        newIngredientEntry = tk.Entry(newBoxesContainer,
            font=('TkDefaultFont 12'),
            bg=COLORS.B02,
            fg=COLORS.B2
        )
        newAmtEntry = tk.Entry(newBoxesContainer,
            font=('TkDefaultFont 12'),
            bg=COLORS.B02,
            fg=COLORS.B2
        )
        addButton = tk.Button(newBoxesContainer, text='Add',
            bg=COLORS.B02,
            activebackground=COLORS.B01,
            fg=COLORS.B2,
            command=lambda:IngredientsWindow.add(
                table,
                newIngredientEntry,
                newAmtEntry,
                selected_food
            )
        )

        editIngredientEntry = tk.Entry(editBoxesContainer,
            font=('TkDefaultFont 12'),
            bg=COLORS.B02,
            fg=COLORS.B2
        )
        editAmtEntry = tk.Entry(editBoxesContainer,
            font=('TkDefaultFont 12'),
            bg=COLORS.B02,
            fg=COLORS.B2
        )
        saveButton = tk.Button(editBoxesContainer, text='Save',
            bg=COLORS.B02,
            activebackground=COLORS.B01,
            fg=COLORS.B2,
            command=lambda:IngredientsWindow.save(
                table,
                editIngredientEntry,
                editAmtEntry,
                selected_food
            )
        )
        rmButton = tk.Button(editBoxesContainer, text='Delete',
            bg=COLORS.B02,
            activebackground=COLORS.B01,
            fg=COLORS.B2,
            command=lambda:IngredientsWindow.rm(
                table,
                editIngredientEntry,
                selected_food
            ))

        #### TABLE ELEMENTS ####
        table = ttk.Treeview(tableContainer,
        padding=[10, 10], 
        columns=('ingredient', 'ammount', 'unit'),
        show='headings',
        selectmode='browse')

        table.heading('ingredient', text='ingredient')
        table.heading('ammount', text='ammount')
        table.heading('unit', text='unit')

        for key, item in Utils.show_ingredients(selected_food).items():
            table.insert('', tk.END, values = (
                key,
                item['ammount'],
                item['unit']
                )
            )

        #### PACKING ####
        container.pack(side=tk.RIGHT, fill = 'both', expand=False)
        tableContainer.pack(fill = 'both', expand=True)

        table.pack(fill='both', expand = True, side=tk.TOP)
        table.bind('<Double-1>', lambda x:IngredientsWindow.select(table, editIngredientEntry))

        newLabel.pack(side=tk.TOP, anchor='w')
        newBoxesContainer.pack(side=tk.TOP, anchor='w')
        newIngredientEntry.pack()
        newAmtEntry.pack()
        addButton.pack(side=tk.BOTTOM, anchor='w')

        editLabel.pack(side=tk.TOP, anchor='w')
        editBoxesContainer.pack(side=tk.TOP, anchor='w')
        editIngredientEntry.pack()
        editAmtEntry.pack()
        saveButton.pack(side=tk.BOTTOM, anchor='w')
        rmButton.pack(side=tk.BOTTOM, anchor='w')