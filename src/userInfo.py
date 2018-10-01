import tkinter
from tkinter import *

import tkinterCommands
import gamesList
import database

#main Window
def window(selected_tuple):

    gamer_ID = selected_tuple[0]
    gamer_tag = selected_tuple[1]
    email = selected_tuple[2]

    def open_games_list():
        gamesList.window(gamer_ID)
        print('back to userinfo')   #debug line
        view_command()
        print('view_comand executed')   #debug line.. both not working

    def get_selected_row(event):
        index = inventory_list.curselection()[0]
        print(index)
        global selected_tuple_games
        selected_tuple_games = inventory_list.get(index)
        print(selected_tuple_games)

    def view_command():
        inventory_list.delete(0, END)
        for row in database.view('inventory'):
            inventory_list.insert(END, row)
    

    user_info = Tk()
    user_info.title('Gamer Info: %s' %gamer_tag)
    print(selected_tuple)       #debug line

    
    tkinterCommands.createLable(user_info, 'Name :', row=0, col=0)
    tkinterCommands.createLable(user_info, gamer_tag, row=0, col=1)
    tkinterCommands.createLable(user_info, 'Email :', row=1, col=0)
    tkinterCommands.createLable(user_info, email, row=1, col=1)

    tkinterCommands.createButton(user_info, 'Add Game', width=12, row=0, col=4, cmd=open_games_list)
    tkinterCommands.createButton(user_info, 'Remove Game', width=12, row=1, col=4, cmd=tkinterCommands.printmessage)
    tkinterCommands.createButton(user_info, 'Delete User', width=12, row=2, col=4, cmd=tkinterCommands.printmessage)
    tkinterCommands.createButton(user_info, 'Refresh', width=12, row=2, col=3, cmd=view_command)

    inventory_list = tkinterCommands.createList(user_info, height=30, width=120, row=5, col=0, columnspan=5)
    inventory_list.bind('<<ListboxSelect>>',get_selected_row)
    view_command()

    user_info.mainloop()
