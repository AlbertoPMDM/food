import tkinter as tk
from src.app.sidebar import Sidebar

class Main(tk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent)
        container1 = tk.Frame(parent, height='600', width='200')
        container2 = tk.Frame(parent, height='600', width='600')
        container1.pack(fill='both', expand=True, side=tk.LEFT)
        container2.pack(fill='both', expand=True, side=tk.RIGHT)
        Sidebar(container1, container2)