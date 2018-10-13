import sqlite3

data_base_name = "MyGameCafe_V2.db"

'''This is the Data Base for the gaming center'''
def connect():
    conn = sqlite3.connect(data_base_name)
    cur = conn.cursor()
    #cur.execute("DROP TABLE if exists gamer")
    cur.execute("CREATE TABLE IF NOT EXISTS gamer(id INTEGER PRIMARY KEY , gamer_tag TEXT, email TEXT, UNIQUE (email))")
    
    #cur.execute("DROP TABLE if exists games")
    cur.execute("CREATE TABLE IF NOT EXISTS games(game_id INTEGER PRIMARY KEY , game_name TEXT, genre TEXT )")
    
    #cur.execute("DROP TABLE if exists inventory")
    cur.execute("CREATE TABLE IF NOT EXISTS inventory(game_ID INTEGER, gamer_ID INTEGER, game_name TEXT, play_time INTEGER, achievments TEXT, PRIMARY KEY(game_ID, gamer_ID))")
    conn.commit
    conn.close()

def view(table_name):
    """Returns all the tuples in any give table_name"""
    conn = sqlite3.connect(data_base_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM %s" % table_name)
    rows = cur.fetchall()
    conn.close()
    print('printing rows: ',rows)
    return rows

def view_inventory(gamer_ID):
    """Returns all the tuples in inventory(table) based on gamer_ID  """
    conn = sqlite3.connect(data_base_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM inventory WHERE gamer_ID = %s" % (gamer_ID))
    rows = cur.fetchall()
    conn.close()
    return rows

def insert(id, gamer_tag, email):
    conn = sqlite3.connect(data_base_name)
    cur = conn.cursor()
    cur.execute("INSERT or REPLACE INTO gamer VALUES (?,?,?)", (id, gamer_tag, email))
    conn.commit()
    conn.close()

def insert_games(game_id, game_name, genre):
    conn = sqlite3.connect(data_base_name)
    cur = conn.cursor()
    cur.execute("INSERT or REPLACE INTO games VALUES (?,?,?)", (game_id, game_name, genre))
    conn.commit()
    conn.close()

def insert_inventory(game_ID, gamer_ID, game_name, play_time, achievments):
    conn = sqlite3.connect(data_base_name)
    cur = conn.cursor()
    cur.execute("INSERT or REPLACE INTO inventory VALUES (?,?,?,?,?)", (game_ID, gamer_ID, game_name, play_time, achievments))
    conn.commit()
    conn.close()

def delete(id):
    connection = sqlite3.connect(data_base_name)
    cur = connection.cursor()
    cur.execute("DELETE FROM gamer WHERE id = ?", (id, ))
    print('Deleted: ', id)
    connection.commit()
    connection.close()

def delete_game(game_ID):
    '''Deletes a game form inventory table'''
    conn = sqlite3.connect(data_base_name)
    cur = conn.cursor()
    cur.execute("DELETE FROM inventory WHERE game_ID = ?", (game_ID, ))
    print('Deleted "%d" game from "games"',id)
    conn.commit()
    conn.close()

connect()
insert(8079, 'Ataa', 'ataago7@gmail.com')
insert(83079, 'Nishant', 'noob@gmail.com')
insert(12379, 'Amit', 'wastefellow@gmail.com')

insert_games(123, 'GTA V', 'Openworld')
insert_games(124, 'Read Dead Redemption', 'Openworld')
insert_games(112, 'Euro Truck Simulator', 'Simulation')
insert_games(432, 'CSGO', 'First person Shooter')
insert_games(654, 'Battlefield', 'First person Shooter')
insert_games(765, 'City Skylines', 'Simulation')
insert_games(234, 'PUBG', 'First person Shooter')

#insert_inventory(123,324,'gta',32,'gold')
#insert_inventory(234,324,'gta',32,'gold')
print(view('gamer'))