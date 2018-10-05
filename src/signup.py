import tkinter
from tkinter import *

import tkinterCommands
import database


unique_ID = 71700

#database commands

def add_gamer_info(gamer_name,gamer_email):
    """Inserting New Gamer data into gamer table"""
    global unique_ID 
    unique_ID += 1
    print(gamer_name,gamer_email)
    database.insert(unique_ID, gamer_name, gamer_email)
    
#main window 
def window():
    """New Window for signing up the new user"""
    new_user = Tk()
    new_user.title("Sign up")
    
    tkinterCommands.createLable(new_user, 'Enter the Following details to signup', row=0, col=0, colspan=2)

    def get_info():
        name = gamer_name_entry.get()
        email = gamer_email_entry.get()
        print(name,' ', email)      #debug line
        add_gamer_info(name,email)
        new_user.destroy()

    tkinterCommands.createLable(new_user, 'Name: ', row=1, col=0)
    gamer_name_entry = tkinterCommands.createEntry(new_user, row=1, col=1)

    tkinterCommands.createLable(new_user, 'Email: ', row=2, col=0)
    gamer_email_entry = tkinterCommands.createEntry(new_user, row=2, col=1)

    tkinterCommands.createButton(new_user, 'Submit', width=12, row=3, col=1, cmd=get_info)
    
    new_user.mainloop()