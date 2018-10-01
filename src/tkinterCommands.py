import tkinter
from tkinter import *
from tkinter import messagebox

def createLable(root, text, row, col, colspan=1):
    label = Label(root, text=text)
    label.grid(row=row, column=col, columnspan=colspan, sticky=W)

def printmessage():
    print('Button Pressed')

def createButton(root, name, width, row, col, cmd):
    printbutton = Button(root, text = name, width=width, command=cmd)
    printbutton.grid(row=row, column=col, sticky=E)

def createList(root, height, width, row, col, rowspan=6, columnspan=4):
    list = Listbox(root, height=height, width=width)
    list.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan)
    sb1 = Scrollbar(root)
    sb1.grid(row=rowspan, column=columnspan, rowspan=30)
    list.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list.yview)
    return list

def createEntry(root, row, col):
    entry = Entry(root)
    entry.grid(row=row, column=col)
    return entry
