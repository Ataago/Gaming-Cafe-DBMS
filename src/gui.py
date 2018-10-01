import tkinter
from tkinter import *
from tkinter import messagebox

import tkinterCommands
import userInfo
import signup
import database


#database commands

def get_selected_row(event):
    index = gamer_list.curselection()[0]
    print(index)
    global selected_tuple
    selected_tuple = gamer_list.get(index)
    print(selected_tuple)

def view_command():
    gamer_list.delete(0, END)
    for row in database.view('gamer'):
        gamer_list.insert(END, row)

def add_gamer_command():
    signup.window()
    view_command()

def remove_gamer_command():
    ID = selected_tuple[0]
    if messagebox.askokcancel('Delete User', 'Are you sure you want to remove %s permenantly?' % selected_tuple[1]):
        database.delete(ID)
    view_command()

def view_gamer_command():
    ID = selected_tuple[0]
    print(ID)
    userInfo.window(selected_tuple)


#main home window GUI

root = Tk()
root.title("My Gaming Cafe Data")


def on_closing():
    if messagebox.askokcancel('Quit', 'Are you sure you want to quit?'):
            root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)


tkinterCommands.createLable(root, 'Nishant Gaming Cafe', row=1, col=1)  #insert image and make it bold

tkinterCommands.createButton(root, 'Refresh', width=12, row=3,col=2, cmd=view_command)
tkinterCommands.createButton(root, 'Add Gamer', width=17, row=1, col=3, cmd = add_gamer_command)
tkinterCommands.createButton(root, 'Remove Gamer',width=17, row=2, col=3, cmd = remove_gamer_command)
tkinterCommands.createButton(root, 'View Gamer', width=17, row=3, col=3, cmd = view_gamer_command)

gamer_list = tkinterCommands.createList(root, height=40, width=100, row=5, col=0)
gamer_list.bind('<<ListboxSelect>>',get_selected_row)

view_command()
root.mainloop()


