import sqlite3

'''This is the Data Base for the gaming center'''
def connect():
    conn = sqlite3.connect("MyGameCafeDB.db")
    cur = conn.cursor()
    cur.execute("DROP TABLE if exists gamer")
    cur.execute("CREATE TABLE IF NOT EXISTS gamer(id INTEGER PRIMARY KEY , gamer_tag TEXT, email TEXT )")
    
    cur.execute("DROP TABLE if exists games")
    cur.execute("CREATE TABLE IF NOT EXISTS games(game_id INTEGER PRIMARY KEY , game_name TEXT, genre TEXT )")
    
    cur.execute("DROP TABLE if exists inventory")
    cur.execute("CREATE TABLE IF NOT EXISTS inventory(game_ID INTEGER PRIMARY KEY , gamer_ID INTEGER, game_name TEXT, play_time INTEGER, achievments TEXT )")
    conn.commit
    conn.close()

#get all gamers
def view(table_name):
    conn = sqlite3.connect("MyGameCafeDB.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM %s" % table_name)
    rows = cur.fetchall()
    conn.close()
    return rows


def insert(id, gamer_tag, email):
    conn = sqlite3.connect("MyGameCafeDB.db")
    cur = conn.cursor()
    cur.execute("INSERT or REPLACE INTO gamer VALUES (?,?,?)", (id, gamer_tag, email))
    conn.commit()
    conn.close()

def insert_games(game_id, game_name, genre):
    conn = sqlite3.connect("MyGameCafeDB.db")
    cur = conn.cursor()
    cur.execute("INSERT or REPLACE INTO games VALUES (?,?,?)", (game_id, game_name, genre))
    conn.commit()
    conn.close()

def insert_inventory(game_ID, gamer_ID, game_name, play_time, achievments):
    conn = sqlite3.connect("MyGameCafeDB.db")
    cur = conn.cursor()
    cur.execute("INSERT or REPLACE INTO inventory VALUES (?,?,?,?,?)", (game_ID, gamer_ID, game_name, play_time, achievments))
    conn.commit()
    conn.close()

def delete(id):
    connection = sqlite3.connect("MyGameCafeDB.db")
    cur = connection.cursor()
    cur.execute("DELETE FROM gamer WHERE id = ?", (id, ))
    print('Deleted: ', id)
    connection.commit()
    connection.close()

connect()
insert(8079, 'Ataa', 'ataago7@gmail.com')
insert(83079, 'Nishant', 'noob@gmail.com')
insert(12379, 'Amit', 'wastefellow@gmail.com')

insert_games(123, 'GTA V', 'Openworld')
insert_games(124, 'Read Dead Redemption', 'Openworld')
insert_games(112, 'Euro Truck Simulator', 'Simulation')
insert_games(153, 'CSGO', 'First person Shooter')

insert_inventory(123,324,'gta',32,'gold')
insert_inventory(234,324,'gta',32,'gold')
print(view('gamer'))