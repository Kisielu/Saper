__author__ = 'pkisielewicz & igawenda'

from tkinter import *
from SaperPckg.logic import Saper


class Window():

    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Saper")
        Button(parent, text="New Game", relief=GROOVE).grid(row=0, columnspan=Saper.boardWidth, sticky=W)
        self.button_creator()

    def button_creator(self):
        col_count = Saper.boardWidth
        row_count = Saper.boardHeight
        for col in range(0, col_count):
            for row in range(0, row_count):
                Button(self.parent, width=2, height=1, relief=GROOVE).grid(row=row+1, column=col, padx=1, pady=1)

root = Tk()
root.resizable(0,0)
window = Window(root)
root.mainloop()