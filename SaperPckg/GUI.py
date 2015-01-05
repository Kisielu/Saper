__author__ = 'igawenda'

from tkinter import *
from SaperPckg.logic import Saper


class Window():

    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Saper")
        Label(parent, text="New Game").grid(row=0)
        frame = Frame(parent, background="black", height=200, width=300)
        frame.grid(row=1)
        self.center_window()
        lol = Saper.boardHeight
        print(lol)

    def center_window(self):
        width = 300
        height = 300
        self_width = self.parent.winfo_screenwidth()
        self_height = self.parent.winfo_screenheight()
        x = (self_width - width)/2
        y = (self_height - height)/2
        self.parent.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def button_creator(self, col_count, row_count):
        lol = Saper.boardHeight
        print(lol)

root = Tk()
window = Window(root)
root.mainloop()