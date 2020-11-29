import sqlite3 as sl

con  = sl.connect("my-test.db")#create new when not exist 

#function for insert data
def insert_data(name,password):
    sql = 'INSERT INTO PASSWORDS (name,pass) VALUES (?, ?)'
    data =[(name,password)]
    with con:
            con.executemany(sql,data)

def show_data():
    data = con.execute('SELECT * FROM PASSWORDS')
    for row in data:
        print(row)

show_data()