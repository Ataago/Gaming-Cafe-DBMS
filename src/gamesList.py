import tkinter
from tkinter import *
import os

import tkinterCommands
import database

imagerow = 0
imagecol = 3
imagerowspan = 11


#main window
def window(gamer_ID):

    def get_selected_row(event):
        index = games_list.curselection()[0]
        print(index)
        global selected_tuple_games
        selected_tuple_games = games_list.get(index)
        print(selected_tuple_games)

        #display image on click
        gameImage = cwd + '/images//'+ str(selected_tuple_games[0]) + '.png'
        imagefile = PhotoImage(file = gameImage)
        print(imagefile)
        label = Label(select_game, image = imagefile)
        label.gameImage = imagefile
        label.grid_forget()
        label.grid(row = imagerow, column = imagecol, rowspan = imagerowspan, columnspan = 1)
        
        #display info on click
        gamesInfo = database.view_games(selected_tuple_games[0])

        game_id = gamesInfo[0][0]
        game_name = gamesInfo[0][1]
        genre = gamesInfo[0][2]
        release_date = gamesInfo[0][3]
        Version = gamesInfo[0][4]
        rating = gamesInfo[0][5]

        
        tkinterCommands.createLable(select_game, 'Genre :', row=1, col=0)
        tkinterCommands.createLable(select_game, genre, row=1, col=1)
        tkinterCommands.createLable(select_game, 'Release Date :', row=2, col=0)
        tkinterCommands.createLable(select_game, release_date, row=2, col=1)
        tkinterCommands.createLable(select_game, 'Version :', row=3, col=0)
        tkinterCommands.createLable(select_game, Version, row=3, col=1)
        tkinterCommands.createLable(select_game, 'IMDB Rating :', row=4, col=0)
        tkinterCommands.createLable(select_game, rating, row=4, col=1)


    def view_command():
        games_list.delete(0, END)
        for row in database.view('games'):
            display_info =(row[0], row[1])
            games_list.insert(END, display_info)
 

    def add_to_inventory():
        game_ID = selected_tuple_games[0]
        game_name = selected_tuple_games[1]
        print(game_ID, gamer_ID,game_name)      #debuy line
        database.insert_inventory(game_ID, gamer_ID,game_name, 0, 'Novice')
        print('Inserted into inventory')
        select_game.destroy()
        
    select_game = Toplevel()
    select_game.title("Games")

    #Game images
    cwd = os.path.dirname(os.path.realpath(__file__))
    gameImage = cwd + '/images/Games.png'
    imagefile = PhotoImage(file = gameImage)
    print(imagefile)
    label = Label(select_game, image = imagefile)
    label.gameImage = imagefile
    label.grid(row = imagerow, column = imagecol, rowspan = imagerowspan, columnspan = 1)

    tkinterCommands.createLable(select_game, 'Select the Game to Add :', row=0, col=0)

    games_list = tkinterCommands.createList(select_game, height=30, width=50, row=5, col=0, rowspan = 5, columnspan=2)
    games_list.bind('<<ListboxSelect>>',get_selected_row)
    view_command()      #debug line

    tkinterCommands.createButton(select_game, 'Add Game', width=12, row=11, col=3, cmd=add_to_inventory, sticky= EW)

    select_game.mainloop()