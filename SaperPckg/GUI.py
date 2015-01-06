__author__ = 'pkisielewicz & igawenda'

from tkinter import *
from SaperPckg.logic import Saper


saper = Saper()


class Window():

    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Saper")
        self.button_creator()

    def button_creator(self):
        button = Button(self.parent, text="New Game", relief=GROOVE, command=saper.new_game)
        button.grid(row=0, columnspan=saper.boardWidth, sticky=W, padx=2, pady=2)
        col_count = saper.boardWidth
        row_count = saper.boardHeight
        for col in range(0, col_count):
            for row in range(0, row_count):
                butt = Button(self.parent, width=2, height=1, relief=GROOVE, command=lambda x=row, y =col: saper.left_click(x, y))
                butt.bind("<Button-3>", lambda x=row, y =col: saper.right_click(x, y))
                butt.grid(row=row+1, column=col)


root = Tk()
root.resizable(0,0)
window = Window(root)
root.mainloop()