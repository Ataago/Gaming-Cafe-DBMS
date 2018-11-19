import tkinter
from tkinter import *
import os

import tkinterCommands
import database


unique_ID = 71700

#database commands

def add_gamer_info(gamer_name,gamer_email,gamer_tag,age):
    """Inserting New Gamer data into gamer table"""
    global unique_ID 
    unique_ID += 1
    print(gamer_name,gamer_email)
    database.insert(unique_ID, gamer_name, gamer_email, gamer_tag, age)
    
#main window 
def window():
    """New Window for signing up the new user"""
    new_user = Toplevel()
    new_user.title("Sign up")
    
    cwd = os.path.dirname(os.path.realpath(__file__))
    
    demoCafe = cwd + '\images\welcome1.png'
    print(demoCafe)
    cafe = PhotoImage(file = demoCafe)
    label = Label(new_user, image = cafe)
    label.grid(row = 0, column = 0, columnspan = 4)
    #tkinterCommands.createLable(new_user, 'Enter the Following details to signup', row=0, col=0, colspan=4)

    def get_info():
        name = gamer_name_entry.get()
        email = gamer_email_entry.get()
        gamer_tag = gamer_tag_entry.get()
        age = gamer_age_entry.get()
        print(name,' ', email,' ',gamer_tag,' ',age)      #debug line
        add_gamer_info(name,email,gamer_tag,age)
        new_user.destroy()

    tkinterCommands.createLable(new_user, 'Name: ', row=1, col=0, sticky=E)
    gamer_name_entry = tkinterCommands.createEntry(new_user, row=1, col=1, width = 100)

    tkinterCommands.createLable(new_user, 'Email: ', row=2, col=0, sticky=E)
    gamer_email_entry = tkinterCommands.createEntry(new_user, row=2, col=1, width = 100)

    tkinterCommands.createLable(new_user, 'Gamer Tag: ', row=3, col=0, sticky=E)
    gamer_tag_entry = tkinterCommands.createEntry(new_user, row=3, col=1, width = 100)

    tkinterCommands.createLable(new_user, 'Age: ', row=4, col=0, sticky=E)
    gamer_age_entry = tkinterCommands.createEntry(new_user, row=4, col=1, width = 100)

    '''tkinterCommands.createLable(new_user, 'Gender: ', row=5, col=0)
    male = Radiobutton(new_user, Text= 'Male', variable = IntVar, value = 1)
    male.config(indicatoron=0, bd=4, width=12)
    female = Radiobutton(new_user, Text= 'Female', variable = IntVar, value = 2)
    male.pack(row = 5, column = 1)
    female.grid(row = 5, column = 2)'''
    
    tkinterCommands.createButton(new_user, 'Submit', width=12, row=5, col=1, cmd=get_info)
    
    new_user.mainloop()