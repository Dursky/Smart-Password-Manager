from tkinter import *
import tkinter.font

import sqlite3 as sl
from time import sleep
con  = sl.connect("databases/passwords.db")#create new when not exist 
cur = con.cursor()
jump_list =[]#List for show data
to_delete = [] #List to delete


def show_data():
        jump_count = 0 
        data = con.execute('SELECT * FROM PASSWORDS')
        for x in data:
            jump_list.append(x)
        #Don't call fetchone() or fetchall()
        data = con.execute('SELECT * FROM PASSWORDS')
        for row in data:
            return("[|Nr:",row[0],"| Name:",row[1],"| Password: ",row[2],"| E-mail: ",row[3],"|]")
            jump_count = jump_count + 1 
            if(len(jump_list) == jump_count):
                break


#main Window using Tk
win = Tk()


win.title("Smart Password Manager")
win.geometry('400x300')
win.configure(background='#CD5C5C')

#voltage = Label(win, text = "voltage")
#voltage.place(x=15, y=100)

B1 = Button(win, text = "Exit", command = show_data)
B1.place(x = 330,y = 260)

B2 = Button(win, text = "Delete data", command = show_data)
B2.place(x = 220,y = 260)

B3 = Button(win, text = "Insert data", command = show_data)
B3.place(x = 120,y = 260)

B4 = Button(win, text = "Show data", command = show_data)
B4.place(x = 20,y = 260)

voltageValues = Label(win, text = show_data)
voltageValues.place(x=200, y=220)
mainloop()