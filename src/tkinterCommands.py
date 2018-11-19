import tkinter
from tkinter import *
from tkinter import messagebox

def createLable(root, text, row, col, colspan=1, sticky=W):
    label = Label(root, text=text)
    label.grid(row=row, column=col, columnspan=colspan, sticky=sticky)

def printmessage():
    print('Button Pressed')

def createButton(root, name, width, row, col, cmd, sticky='E'):
    printbutton = Button(root, text = name, width=width, command=cmd)
    printbutton.grid(row=row, column=col, sticky=sticky)

def createList(root, height, width, row, col, rowspan=100, columnspan=4):
    sb1 = Scrollbar(root)
    sb1.grid(row=rowspan, column=columnspan, rowspan=rowspan)
    list = Listbox(root, height=height, width=width, yscrollcommand = sb1.set)
    list.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan)
    list.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list.yview)
    return list

def createEntry(root, row, col, width = 17):
    entry = Entry(root, width = width)
    entry.grid(row=row, column=col, columnspan = 2)
    return entry
