import mysql.connector
from mysql.connector import Error

#AWS database connection
def create_con(hostname, username, userpw, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=hostname,
            user=username,
            password=userpw,
            database=dbname
        )
        print("Connection Succesfull")
    except Error as e:
        print(f'The error {e} occured!')
    return connection

conn = create_con('cis3668springdb.c7q6qpy7poi5.us-east-1.rds.amazonaws.com', 'admin', 'password123', 'cis3668springdb')
cursor = conn.cursor(dictionary = True)
sql = "Select * from fish"
cursor.execute(sql)
rows = cursor.fetchall()
#Creating menu for the command line interface
def menu():
    print("MENU")
    print("a - Add fish")
    print("o - Output all fish in console")
    print("q - Quit\n")
#requesting user input
menu()
user_input = input("Enter an input: ")
#creating lists to hold values
x = []
y = []
z = []
v = []
w = []
#functions to add specificaitons to fish
def add_fish_class():
    x = input("Enter a class of fish:")
    print(x)
    

def add_fish_species():
    y = input("Enter a specie of fish:")
    print(y)



def add_fish_color():
    w = input("Enter color of fish:")
    print(w)




def add_fish_acquired():
    z = input("Is this fish acquired? Yes/No:")
    print(z)



def add_fish_dead_or_alive():
    v = input("Is this fish alive? Yes/No/Unkown:")
    print(v)


#loop through options until user reaches q
while user_input != "q":
    if user_input == "a":
        add_fish_class()
        add_fish_species()
        add_fish_color()
        add_fish_acquired()
        add_fish_dead_or_alive()
        sql = 'insert into fish (id, superclass, species, acquired, alive) values (id, superclass, species, acquired, alive)'
        print("fish added")

    elif user_input == "o":  
        sql = 'select * from fish'
        for fish in rows:
            print(fish)

    elif user_input == "q":
        break
#if use inputs anything other than a, o, or q prints invalid
    else:
        print("invalid")
#prints out the menu at the start of the program
    print()
    menu()

    user_input = input("Enter an input:\n")
