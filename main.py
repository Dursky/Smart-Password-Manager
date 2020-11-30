import sqlite3 as sl
from time import sleep
con  = sl.connect("databases/passwords.db")#create new when not exist 
cur = con.cursor()
jump_list =[]#List for show data
#main menu show
def main_menu():
    print("=======================")
    print("|What you want to do ?|")
    print("|1 - Show data from db|")
    print("|2 - Insert data to db|")
    print("|3 - Insert data to db|")
    print("|4 - Exit|")
    choose =int(input("=======================\n"))
    if(choose == 1):
        show_data()
        sleep(0.5)
        main_menu()
    if(choose == 2 ):
        name = str(input("Type a name:\n"))
        password = str(input("Type a password:\n"))
        email = str(input("Type a email:\n"))
        insert_data(name,password,email)
        main_menu()
    if(choose == 4):
        delete_record()
    if(choose == 4):
        exit_program()


#function for insert data
def insert_data(name,password,email):
    sql = 'INSERT INTO PASSWORDS (name,pass,email) VALUES (?, ?,?)'
    data =[(name,password,email)]
    with con:
            con.executemany(sql,data)
#function for exit_program
def exit_program():
    print("Goodbye!")
    exit()

#Data show function
def show_data():

        jump_count = 0 
        data = con.execute('SELECT * FROM PASSWORDS')
        for x in data:
            jump_list.append(x)
        #Don't call fetchone() or fetchall()
        data = con.execute('SELECT * FROM PASSWORDS')
        for row in data:
            print("[|Nr:",len(jump_list),"| Name:",row[1],"| Password: ",row[2],"| E-mail: ",row[3],"|]")
            jump_count = jump_count + 1 
            if(len(jump_list) == jump_count):
                break
        else:
            create = int(input("What you want to do?\n1 - Create\n2 - Return to menu\n"))
            if(create == 1):
                print("Type a name, password and e-mail for service:\n")
                name = input("Name: ")
                password = input("Password: ")
                email = input("E-mail: ")
                sure = int(input("Are you sure?\n1 - Yes\n2 - No\n"))
                if(sure == 1):
                    insert_data(name,password,email)
                    print("Sucess!")
                    main_menu()
                if(sure == 2):
                    main_menu()
            if(create == 2 ):
                main_menu()

def delete_record():
    print("What do you want to delete?")
    number_record = int(input("You have a:",len(jump_list)))
   # make a automate global if
    #if(number_record == )
main_menu()