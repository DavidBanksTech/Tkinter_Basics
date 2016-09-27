from tkinter import *
from tkinter import ttk

root = Tk()
lb = Listbox(root, height = 3)
lb.grid(row = 0, column = 0)
lb.insert(END, 'First Entry')
lb.insert(END, 'Second Entry')
lb.insert(END, 'Third Entry')
lb.insert(END, 'Fourth Entry')

sb = Scrollbar(root, orient = VERTICAL)
sb.grid(row = 0, column = 1)

sb.configure(command = lb.yview)
lb.configure(yscrollcommand = sb.set)



