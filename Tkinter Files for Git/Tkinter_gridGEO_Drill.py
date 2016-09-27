from tkinter import *
from tkinter import ttk

root = Tk()

b1 = Button(root, text = 'One')
b2 = Button(root, text = 'Two')
b1.grid( row = 0, column = 0)
b2.grid( row = 1, column = 1)

l = Label( root, text = 'This is a label')
l.grid( row = 1, column = 0)

