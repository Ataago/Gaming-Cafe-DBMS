import tkinter
from tkinter import *

import tkinterCommands
import database



#main window
def window(gamer_ID):

    def get_selected_row(event):
        index = games_list.curselection()[0]
        print(index)
        global selected_tuple_games
        selected_tuple_games = games_list.get(index)
        print(selected_tuple_games)

    def view_command():
        games_list.delete(0, END)
        for row in database.view('games'):
            games_list.insert(END, row)

    def add_to_inventory():
        game_ID = selected_tuple_games[0]
        game_name = selected_tuple_games[1]
        print(game_ID, gamer_ID,game_name)      #debuy line
        database.insert_inventory(game_ID, gamer_ID,game_name, 0, 'Gold')
        print('Inserted into inventory')
        select_game.destroy()
        
    select_game = Tk()
    select_game.title("Games")

    tkinterCommands.createLable(select_game, 'Select the Game to Add :', row=0, col=0)

    games_list = tkinterCommands.createList(select_game, height=30, width=120, row=5, col=0, columnspan=5)
    games_list.bind('<<ListboxSelect>>',get_selected_row)
    view_command()      #debug line

    tkinterCommands.createButton(select_game, 'Add Game', width=12, row=30, col=1, cmd=add_to_inventory)

    select_game.mainloop()