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

conn = create_con('Inset_AWS_DATABASE_ENDPOINT', 'admin', 'password123', 'cis3668springdb')
cursor = conn.cursor(dictionary = True)
sql = "Select * from fish"
cursor.execute(sql)
rows = cursor.fetchall()
