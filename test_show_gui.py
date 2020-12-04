#data getting is a list eg. [10, 12]
from tkinter import *
import tkinter.font


#main Window using Tk
win = Tk()

win.title("v1.0")
win.geometry('800x480')
win.configure(background='#CD5C5C')

#Labels
voltage = Label(win, text = "voltage")
voltage.place(x=15, y=100)

current = Label(win, text = "current")
current.place(x=15, y=200)

#display measured values
#how to display here !!!
currentValues = Label(win, text = "want to display somewhere like this")
currentValues.place(x=200, y=100)

voltageValues = Label(win, text = 123)
voltageValues.place(x=200, y=200)
mainloop()