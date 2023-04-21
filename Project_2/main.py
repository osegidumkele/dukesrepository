class Creds:
    constring = 'INSERT_AWS_DB_ENDPOINT'
    userName = 'admin'
    password = 'password123
    dbName = 'cis3368spring'
   
  
import mysql.connector
import creds
from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

#SQL CONNECTION
myCreds = creds.Creds()
conn = create_connection(myCreds.constring, myCreds.userName, myCreds.password, myCreds.dbName)

#INSERT INTO TABLE QUERY
query = "INSERT INTO snowboard (boardtype, brand, msrp, size) VALUES ('all_mountain', 'burton', '1499', '20_inches')"
execute_query(conn, query)

#Select all snowboards
select_users = "SELECT * FROM snowboard"
gem = execute_read_query(conn, select_users)

for user in users:
  print(snowboard["boardtype"] + " snowboards by: " + snowboard["brand"] " cost " + snowboard["msrp"] " at msrp and are " + snowboard["size"])
  
  
# ADD TABLE QUERY
create_snowboard_table = """
Create table snowboard (id int(6) PRIMARY KEY AUTO_INCREMENT NOT NULL,
                    boardtpe varchar(255),
                    brand varchar(255),
                    msrp varchar(255),
                    size varchar(255)
                    )"""

execute_query(conn, create_snowboard_table)

id = 1
boardtype = "all_mountain"
brand = "Burton"
msrp =  495
size = "20_inches"

query = "INSERT INTO snowboard (id, boardtype, brand, msrp, size) VALUES (%s, %s, %s, %s, %s)" % (id, boardtype, brand, msrp, size)

execute_query(conn, query)
#UPDATE STATEMENT

new_msrp = 1500
update_snowboard_query = """
UPDATE snowboard
SET msrp = %s
WHERE id = 1 """ % (new_msrp)

execute_query(conn, update_snowboard_query)

#DELETE STATEMENT for deleting snowboards from the table
snowboard_id_to_delete = 1
delete_statement = "DELETE FROM invoices WHERE id = %s" % (snowboard_id_to_delete)
execute_quer(conn, delete_statement)

#DELETE STATEMENT for deleting entire snowboard table
delete_snowboard_table = "DROP TABLE snowboard"
execute_query(conn, delete_snowboard_table)
