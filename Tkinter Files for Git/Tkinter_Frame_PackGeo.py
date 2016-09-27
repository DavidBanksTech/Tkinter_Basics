from tkinter import *
from tkinter import ttk

root = Tk()

f = Frame(root)
b1 = Button(f, text = "One")
b2 = Button(f, text = "Two")
b3 = Button(f, text = "Three")

b1.pack(side = LEFT)
b2.pack(side = LEFT)
b3.pack(side = LEFT)

l = Label(root, text = 'This label is packed on top')

l.pack()
f.pack()
