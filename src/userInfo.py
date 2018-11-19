import tkinter
from tkinter import *
from tkinter import messagebox

import tkinterCommands
import gamesList
import database

#main Window
def window(selected_tuple):
    gamer_info = database.view_gamer(selected_tuple[0])
    print('Selected Gamer: ',gamer_info)


    gamer_ID = gamer_info[0][0]
    gamer_tag = gamer_info[0][1]
    email = gamer_info[0][2]
    tag = gamer_info[0][3]
    age = gamer_info[0][4]

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
        for row in database.view_inventory(gamer_ID):
            inventory_list.insert(END, row)

    def remove_game_command():
        if messagebox.askokcancel('Delete Game', 'Are you sure you want to remove %s permenantly from %s?' % (selected_tuple_games[2],gamer_tag) ):
            database.delete_game(selected_tuple_games[0])
        view_command()
        
    user_info = Tk()
    user_info.title('Gamer Info: %s' %gamer_tag)
    print(selected_tuple)       #debug line
    
    def remove_gamer_command():
        if messagebox.askokcancel('Delete User', 'Are you sure you want to remove %s permenantly?' % gamer_tag):
            database.delete(gamer_ID)
            user_info.destroy()
        
    tkinterCommands.createLable(user_info, 'Name :', row=0, col=0)
    tkinterCommands.createLable(user_info, gamer_tag, row=0, col=1)
    tkinterCommands.createLable(user_info, 'Email :', row=1, col=0)
    tkinterCommands.createLable(user_info, email, row=1, col=1)
    tkinterCommands.createLable(user_info, 'Gamer Tag :', row=2, col=0)
    tkinterCommands.createLable(user_info, tag, row=2, col=1)
    tkinterCommands.createLable(user_info, 'Age :', row=3, col=0)
    tkinterCommands.createLable(user_info, age, row=3, col=1)

    tkinterCommands.createButton(user_info, 'Add Game', width=12, row=0, col=4, cmd=open_games_list)
    tkinterCommands.createButton(user_info, 'Remove Game', width=12, row=1, col=4, cmd=remove_game_command )
    tkinterCommands.createButton(user_info, 'Delete User', width=12, row=2, col=4, cmd=remove_gamer_command)
    tkinterCommands.createButton(user_info, 'Refresh', width=12, row=2, col=3, cmd=view_command)

    inventory_list = tkinterCommands.createList(user_info, height=30, width=120, row=5, col=0, columnspan=5)
    inventory_list.bind('<<ListboxSelect>>',get_selected_row)
    view_command()

    user_info.mainloop()
