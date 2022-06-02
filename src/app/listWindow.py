import tkinter as tk
from tkinter import ttk

from src.utils.utils import Utils
from src.program.program import Foodlist
from src.database.database import Foods

from src.app.colors import COLORS

class ListWindow(tk.Toplevel):

    FoodList:dict[str,int]={}

    def export()-> None:
        tmp_list = []
        for key,item in ListWindow.FoodList.items():
            tmp_list += [key]*item
        Foodlist(tmp_list).export()

    def select(table:ttk.Treeview, food:tk.Entry)-> None:
        food.delete(0, tk.END)
        item = table.item(table.selection()[0])['values'][0]
        food.insert(0, item)

    def add(table:ttk.Treeview, food:tk.Entry, amt:tk.Entry)->None:
        table.insert('', tk.END, values = (
                food.get(),
                int(amt.get()),
            )
        )
        ListWindow.FoodList[food.get()] = int(amt.get())
        food.delete(0,tk.END)
        amt.delete(0,tk.END)

    def save(table:ttk.Treeview, food:tk.Entry, amt:tk.Entry)->None:
        selected_item = table.selection()[0]
        table.set(selected_item, 1, int(amt.get()))
        ListWindow.FoodList[food.get()] = int(amt.get())
        food.delete(0,tk.END)
        amt.delete(0,tk.END)

    def rm(table:ttk.Treeview, food:tk.Entry)->None:
        selected_item = table.selection()[0]
        del ListWindow.FoodList[food.get()]
        table.delete(selected_item)
        food.delete(0,tk.END)

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ingredients")

        #### CONTAINERS ####
        tableContainer = tk.Frame(self, height='600', width='700')

        container = tk.Frame(self, height='600', width='300', bg=COLORS.B03, padx=10, pady=10)

        newBoxesContainer = tk.Frame(container,
            bg=COLORS.B02, 
            highlightbackground=COLORS.RED,
            highlightthickness=3
        )
        editBoxesContainer = tk.Frame(container,
            bg=COLORS.B02, 
            highlightbackground=COLORS.YELLOW,
            highlightthickness=3
        )


        #### OTHER ELEMENTS ####
        newLabel = tk.Label(container, text='New',
            bg=COLORS.B03,
            fg=COLORS.RED,
        )
        editLabel = tk.Label(container, text='Edit',
            bg=COLORS.B03,
            fg=COLORS.YELLOW,
        )

        newFoodEntry = tk.Entry(newBoxesContainer,
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
            command=lambda:ListWindow.add(
                table,
                newFoodEntry,
                newAmtEntry,
            )
        )

        editFoodEntry = tk.Entry(editBoxesContainer,
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
            command=lambda:ListWindow.save(
                table,
                editFoodEntry,
                editAmtEntry,
            )
        )
        rmButton = tk.Button(editBoxesContainer, text='Delete',
            bg=COLORS.B02,
            activebackground=COLORS.B01,
            fg=COLORS.B2,
            command=lambda:ListWindow.rm(
                table,
                editFoodEntry,
            ))
        expButton = tk.Button(editBoxesContainer, text='Export',
            bg=COLORS.B02,
            activebackground=COLORS.B01,
            fg=COLORS.B2,
            command=lambda:ListWindow.export()
        )

        #### TABLE ELEMENTS ####
        table = ttk.Treeview(tableContainer,
        padding=[10, 10], 
        columns=('food', 'ammount'),
        show='headings',
        selectmode='browse')

        table.heading('food', text='food')
        table.heading('ammount', text='ammount')

        for item in ListWindow.FoodList:
            table.insert('', tk.END, values = (
                item[0],
                item[1]
                )
            )

        #### PACKING ####
        container.pack(side=tk.RIGHT, fill = 'both', expand=False)
        tableContainer.pack(fill = 'both', expand=True)

        table.pack(fill='both', expand = True, side=tk.TOP)
        table.bind('<Double-1>', lambda x:ListWindow.select(table, editFoodEntry))

        newLabel.pack(side=tk.TOP, anchor='w')
        newBoxesContainer.pack(side=tk.TOP, anchor='w')
        newFoodEntry.pack()
        newAmtEntry.pack()
        addButton.pack(side=tk.BOTTOM, anchor='w')

        editLabel.pack(side=tk.TOP, anchor='w')
        editBoxesContainer.pack(side=tk.TOP, anchor='w')
        editFoodEntry.pack()
        editAmtEntry.pack()
        saveButton.pack(side=tk.BOTTOM, anchor='w')
        rmButton.pack(side=tk.BOTTOM, anchor='w')
        expButton.pack(side=tk.BOTTOM, anchor='w')