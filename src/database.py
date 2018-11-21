import sqlite3

data_base_name = "MyGameCafe_V2.db"

'''This is the Data Base for the gaming center'''
def connect():
    conn = sqlite3.connect(data_base_name)
    cur = conn.cursor()
    '''
    cur.execute("drop table test")
    cur.execute("create table if not exists test(id integer)")
    cur.execute("insert into test values('asdfas')")
    conn.commit()
    cur.execute("delete from owner where username = ''")
    print('Deleted')
    rows = cur.fetchall()
    print(rows)
    '''
    #cur.execute("DROP TABLE IF EXISTS owner")
    cur.execute("CREATE TABLE IF NOT EXISTS owner(username TEXT NOT NULL, password TEXt NOT NULL, UNIQUE(username));")

    #cur.execute("DROP TABLE if exists gamer")
    cur.execute("CREATE TABLE IF NOT EXISTS gamer(id INTEGER PRIMARY KEY , gamer_name TEXT, email TEXT, gamer_tag TEXT, age INTEGER, UNIQUE (email))")
    
    #cur.execute("DROP TABLE if exists games")
    cur.execute("CREATE TABLE IF NOT EXISTS games(game_id INTEGER PRIMARY KEY , game_name TEXT, genre TEXT, release_date DATE, Version INTEGER, rating INTEGER )")
    
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
    return rows

def view_owner(username):
    """returns the tuple with username and password"""
    conn = sqlite3.connect(data_base_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM owner WHERE username = '%s' " % (username))
    rows = cur.fetchall()
    conn.close()
    return rows

def view_gamer(gamer_ID):
    """returns the tuple based on gamer 'id'"""
    conn = sqlite3.connect(data_base_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM gamer WHERE id = %s" % (gamer_ID))
    rows = cur.fetchall()
    conn.close()
    return rows

def view_inventory(gamer_ID):
    """Returns all the tuples in inventory(table) based on gamer_ID  """
    conn = sqlite3.connect(data_base_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM inventory WHERE gamer_ID = %s" % (gamer_ID))
    rows = cur.fetchall()
    conn.close()
    return rows

def view_games(game_ID):
    """Returns the tuple based on the game_id"""
    conn = sqlite3.connect(data_base_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM games WHERE game_id = %s" % (game_ID))
    rows = cur.fetchall()
    conn.close()
    return rows
    
def insert_owner(username, password):
    conn = sqlite3.connect(data_base_name)
    cur = conn.cursor()
    cur.execute("INSERT or REPLACE INTO owner VALUES (?,?)", (username, password))
    print('inserted')
    conn.commit()
    conn.close()

def insert(id, gamer_name, email, gamer_tag, age):
    conn = sqlite3.connect(data_base_name)
    cur = conn.cursor()
    cur.execute("INSERT or REPLACE INTO gamer VALUES (?,?,?,?,?)", (id, gamer_name, email, gamer_tag, age))
    conn.commit()
    conn.close()

def insert_games(game_id, game_name, genre, release_date , Version , rating  ):
    conn = sqlite3.connect(data_base_name)
    cur = conn.cursor()
    cur.execute("INSERT or REPLACE INTO games VALUES (?,?,?,?,?,?)", (game_id, game_name, genre, release_date, Version, rating))
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

def update_owner(username, password):
    conn = sqlite3.connect(data_base_name)
    cur = conn.cursor()
    cur.execute("UPDATE owner SET password = '%s' WHERE username = '%s'" % (password,username))
    conn.commit()
    conn.close()

#database commands
connect()
"""
insert_owner('ataa','pass')
update_owner('ataa','123')
insert(8079, 'Ataa', 'ataago7@gmail.com','Ataago',19)
insert(83079, 'Nishant', 'noob@gmail.com','Nish',20)
insert(12379, 'Amit', 'wastefellow@gmail.com', '@mit',21)"""


insert_games(123, 'GTA V', 'Openworld  ', '17th Sep, 2013',5, 92)
insert_games(101, 'Battlefield 4', 'Shooter     ','29th Oct, 2013', 4, 77)
insert_games(102, 'Battlefield V', 'Shooter     ','20th Nov, 2018', 5, 'NA')
insert_games(103, 'Grand Theft Auto IV', 'Adventure     ','29th Apr, 2008', 4, 83)
insert_games(104, 'Grand Theft Auto: San Andreas', 'Adventure     ','26th Oct, 2004', 3, 91)
insert_games(105, 'Farming Simulator 19', 'Simulator       ','20th Nov, 2018', 1, 'NA')
insert_games(106, 'Farming Simulator 17', 'Simulator       ','25th Oct, 2016', 5, 90)
insert_games(107, 'Red Dead Redemption', 'Adventure       ','18th May, 2010', 2, 91)
insert_games(108, 'Read Dead Redemption 2', 'Adventure   ','26th Oct, 2018',2,99)
insert_games(109, "PLAYERUNKNOWN'S BATTLEGROUNDS", 'Shooter       ','20th Dec, 2017', 8, 85)
insert_games(110, 'Assassins Creed III', 'Strategy       ','30th Oct, 2012', 5, 73)
insert_games(111, 'Assassins Creed', 'Strategy       ','13th Nov, 2007', 6, 74)
insert_games(112, 'The Witcher 3: Wild Hunt', 'Adventure       ','19th May, 2015', 4, 97)
insert_games(113, 'The Witcher 2: Assassins of Kings', 'Adventure       ','17th May, 2011', 4, 87)
#insert_games(____, '___________', '___________       ','_________', ____, _______)

