import tkinter as tk
from tkinter import ttk
from tkinter import font

from src.app.sidebar import Sidebar
from src.app.colors import COLORS

class Main(tk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent)
        default_font = font.nametofont("TkDefaultFont", self)
        default_font.configure(size=11)
        style = ttk.Style()
        style.theme_use('alt')
        style.configure("Treeview", 
            foreground=COLORS.B2, 
            background=COLORS.B02,
            font = ('TkDefaultFont', 12)
        )
        style.configure("Treeview.Heading", 
            foreground=COLORS.B2, 
            background=COLORS.B02,
            font = ('TkDefaultFont', 12)
        )
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

        container1 = tk.Frame(parent, height='600', width='200')
        container2 = tk.Frame(parent, bg=COLORS.B02,height='600', width='1000')
        container1.pack(fill='both', expand=False, side=tk.LEFT)
        container2.pack(fill='both', expand=True, side=tk.RIGHT)
        container1.pack_propagate(0)
        container2.pack_propagate(0)
        Sidebar(container1, container2)