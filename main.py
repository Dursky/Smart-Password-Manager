import sqlite3 as sl

con  = sl.connect("my-test.db")#create new when not exist 

with con:
    con.execute("""
    CREATE TABLE PASSWORDS (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        pass VARCHAR
    );
    """)


