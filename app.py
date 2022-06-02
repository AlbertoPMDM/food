import tkinter as tk
from src.app.main import Main

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # self.geometry('1200x600')

if __name__ == '__main__':
    app = App()
    Main(app)
    app.mainloop()