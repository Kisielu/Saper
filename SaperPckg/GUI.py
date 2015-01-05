__author__ = 'pkisielewicz & igawenda'

from tkinter import *
from SaperPckg.logic import Saper


class Window():

    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Saper")
        Button(parent, text="New Game", relief=GROOVE).grid(row=0)
        self.center_window()
        self.button_creator()

    def center_window(self):
        width = 275
        height = 250
        self_width = self.parent.winfo_screenwidth()
        self_height = self.parent.winfo_screenheight()
        x = (self_width - width)/2
        y = (self_height - height)/2
        self.parent.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def button_creator(self):
        col_count = Saper.boardWidth
        row_count = Saper.boardHeight
        for col in range(0, col_count):
            for row in range(0, row_count):
                Button(self.parent, width=2, height=1, relief=GROOVE).grid(row=row+1, column=col+1)

root = Tk()
root.resizable(0,0)
window = Window(root)
root.mainloop()