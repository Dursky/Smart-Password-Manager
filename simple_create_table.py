import sqlite3 as sl

con  = sl.connect("databases/passwords.db")#create new when not exist 
con.execute('''CREATE TABLE PASSWORDS
             (ID INTEGER PRIMARY KEY    AUTOINCREMENT,
                name VARCHAR ,
                pass VARCHAR,
                email VARCHAR
                )''')  
print("Table create sucessfull")

con.close()