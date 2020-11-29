import sqlite3 as sl

con  = sl.connect("my-test.db")#create new when not exist 
cur = con.cursor()

#main menu show
def main_menu():
    print("=======================")
    print("|What you want to do ?|")
    print("|1 - Show data from db|")
    print("|2 - Insert data to db|")
    print("|3 - Exit|")
    choose =int(input("=======================\n"))
    if(choose == 1):
        show_data()
        chose_a = int(input("Go to menu ?\n1 - Yes\n2 - No\n"))
        if(chose_a ==1):
            main_menu()
        if(chose_a==2):
           exit_program()
    if(choose == 2 ):
        name = str(input("Type a name:\n"))
        password = str(input("Type a password:\n"))
        insert_data(name,password)
    if(choose == 3):
        exit_program()


#function for insert data
def insert_data(name,password):
    sql = 'INSERT INTO PASSWORDS (name,pass) VALUES (?, ?)'
    data =[(name,password)]
    with con:
            con.executemany(sql,data)
#function for exit_program
def exit_program():
    print("Goodbye!")
    exit()

#Data show function
def show_data():
        jump_list =[]
        jump_count = 0 
        data = con.execute('SELECT * FROM PASSWORDS')
        for x in data:
            jump_list.append(x)
        #Don't call fetchone() or fetchall()
        data = con.execute('SELECT * FROM PASSWORDS')
        for row in data:
            print(row)
            jump_count = jump_count + 1 
            if(len(jump_list) == jump_count):
                break
        else:
            create = int(input("What you want to do?\n1 - Create\n2 - Return to menu\n"))
            if(create == 1):
                print("Type a name and password for service:\n")
                name = input("Name: ")
                password = input("Password: ")
                sure = int(input("Are you sure?\n1 - Yes\n2 - No\n"))
                if(sure == 1):
                    insert_data(name,password)
                    print("Sucess!")
                    main_menu()
                if(sure == 2):
                    main_menu()
            if(create == 2 ):
                main_menu()

def delete_record():
    pass
main_menu()