import sqlite3

class GameDatabase():
        '''This is the Data Base for the gaming center'''
        def __init__(self):
            self.conn = sqlite3.connect("MyGameCafeDB")
            self.cur = self.conn.cursor()
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS gamer(id INTEGER PRIMARY KEY, gamer_tag TEXT, email TEXT )"
            )
            self.conn.commit
        
        def __del__(self):
            self.conn.close()

        #get all gamers
        def view(self):
            self.cur.exectute("SELECT * FROM gamer")
            rows = self.cur.fetchall()
            return rows

        def insert(self, id, gamer_tag, email):
            self.cur.execute("INSERT INTO gamer VALUES(?,?,?)", (id, gamer_tag, email))
            self.conn.commit()

