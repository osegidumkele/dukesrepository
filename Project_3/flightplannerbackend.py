import hashlib
from sql import create_connection 
from sql import execute_query
from sql import execute_read_query
import flask
from flask import jsonify
from flask import request,make_response
from sql import create_connection, execute_read_query,execute_query
from datetime import datetime

conn = create_connection('INSERT_DB_ENDPOINT','admin','admin111','cis3368db') #MySQL and DB connection
app = flask.Flask(__name__) #Flask app initilization
app.config["DEBUG"] = True 

@app.route('/',methods=['GET'])
def homepage():
    return "<h1>WELCOME TO OUR FLIGHT PLANNER</h1>"

# GET route for airports
@app.route('/api/airport/all',methods=['GET']) #Creates get request for all airports
def airport():
    airport = [] #Hold all the SQL results
    sql_select = "SELECT * FROM airport" #command to get all the airports
    port = execute_read_query(conn,sql_select) #Executes SQL
    for port in airport:
        airport.append(port) #Adds to airports list
    return jsonify(port) #Turns list into JSON


# POST for plane
@app.route('/api/plane',methods=['POST']) #Adds new plane to plane table
def add_plane():
    request_data = request.get_json() #Allows data to added in JSON format
    new_planeid = request_data['planeid'] #planeid to add
    new_make = request_data['make'] #make to add
    new_model = request_data['model'] #model to add
    new_year = request_data['year']  #year to add 
    new_capacity = request_data['capacity']  #capacity to add 


    add_sql = f"INSERT INTO plane VALUES (id,'{new_planeid}','{new_make}','{new_model}','{new_year}', {new_capacity})"  #Turns JSON data to SQL insert
    execute_query(conn,add_sql)

    return "NEW PLANE ADDED"

@app.route('/api/airport',methods=['PUT']) #link: http://127.0.0.1:5000/api/airport?id=[ID of your choosing]
def change_airport():
    if 'id' in request.args:
        id=int(request.args['id'])
        request_data = request.get_json(id)
        id = request_data['id'] #id to be updated
        airportcode = request_data['airportcode'] #airportcode to be updated
        airportname = request_data['airportname'] #airportname to be updated
        country = request_data['country']  #country to be updated
        update_dest_sql = f"UPDATE airport SET id='{id}',airportcode='{airportcode}',airportname='{airportname}',country='{country}' WHERE id={id}"
        execute_query(conn,update_dest_sql)
        
    else:
        return 'NO ID GIVEN TO UPDATE' #If there is no ID in the API url this is returned.
    return 'AIRPORT UPDATED' #Confirms that airport is updated.

@app.route('/api/airport',methods=['DELETE']) #link: http://127.0.0.1:5000/api/airport?id=[ID of your choosing]
def del_airport():
    if 'id' in request.args:
        id=int(request.args['id']) #Allows user to user ID as parameter.
    else:
        return "NO ID GIVEN TO DELETE" #If no ID parameter is given this is returned
    delete_airport_sql = f"DELETE FROM airport WHERE id={id}" #Runs SQL statment using the id parameter as WHERE constraint. 
    execute_query(conn,delete_airport_sql) 

    return f"airport WITH ID:{id} DELETED" #Delete conformation


@app.route('/api/plane/all',methods=['GET']) #Creates get request for all planes
def get_plane():
    plan = [] #Houses the SQL results
    sql_select = "SELECT * FROM Trip" #SQL command to get all trips
    plan = execute_read_query(conn,sql_select) #Executes SQL
    for p in plan:
        plan.append(p) #Adds SQL records to trip list
    return jsonify(plan) #Turns list into JSON

@app.route('/api/flights',methods=['GET'])  
def get_flight():
    flight = [] #get the sql 
    sql_select = "SELECT * FROM flights" #SQL command to get all flights
    flight = execute_read_query(conn,sql_select) #Executes SQL
    for air in flight:
        flight.append(air) #Adds SQL records to flights list

#CREATED A NEW JSON WITHIN GET REQUESTS BECAUSE IT WOULD NOT CHANGE WHEN I USED A POST METHOD.

    if 'id' in request.args:  #Checks if and id is given in api parameters
        id = int(request.args['id']) #ID in parameter to be compared later in for loop.
    else:
        return "NO ID GIVEN" #If there is not ID in the parameter this will be returned.
    result = [] #All the results will be placed here
    for air in flight: #For loop iterates through flight list in line 20
        if air['id'] == id: 
            result.append(air) #Adds record in result list if the id matches the parameter.
    return jsonify(result) #Turns the results list into JSON 

@app.route('/api/flights',methods=['POST']) #Adds new plane to plane table
def add_plane():
    request_data = request.get_json() #Allows data to added in JSON format
    new_planeid = request_data['planeid'] #planeid to add
    new_airportfromid = request_data['make'] #airportfrom to add
    new_airporttoid = request_data['model'] #airportto to add
    new_date = request_data['year']  #date to add 

    add_sql = f"INSERT INTO Destination VALUES (id,'{new_planeid}','{new_airportfromid}','{new_airporttoid}','{new_date}')"  #Turns JSON data to SQL insert
    execute_query(conn,add_sql)

    return "NEW FLIGHT ADDED"

@app.route('/api/plane',methods=['PUT']) # link: http://127.0.0.1:5000/api/plane?id=[ID of your choosing]
def change_plane_itinerary():
    if 'id' in request.args:
        id=int(request.args['id'])
        request_data = request.get_json()
        up_capacity = request_data['capacity'] #planeid to add
        up_make = request_data['make'] #make to add
        up_model = request_data['model'] #make to add
        up_year = request_data['year']  #year to add 
        update_plane_sql = f"UPDATE plane SET capacity={up_capacity}, make='{up_make}',model='{up_model}',year='{up_year}', WHERE id={id}"
        execute_query(conn,update_plane_sql)
        
    else:
        return 'NO ID GIVEN TO UPDATE' #If there is no ID in the API url this is returned.
    return 'plane UPDATED' #Confirms that plane is updated.

@app.route('/api/plane',methods=['DELETE']) #Can be tested by using link like this: http://127.0.0.1:5000/api/plane?id=[ID of your choosing]
def del_plane():
    if 'id' in request.args:
        id=int(request.args['id']) #Allows user to user ID as parameter.
    else:
        return "NO ID GIVEN TO DELETE" #If no ID parameter is given 
    delete_plane_sql = f"DELETE FROM plane WHERE id={id}" #Runs SQL statment using the id param as WHERE constraint. 
    execute_query(conn,delete_plane_sql) 

    return f" plane WITH ID:{id} DELETED" #Delete conformation

@app.route('/api/flights',methods=['DELETE']) #Can be tested by using link like this: http://127.0.0.1:5000/api/flights?id=[ID of your choosing]
def del_flights():
    if 'id' in request.args:
        id=int(request.args['id']) #Allows user to user ID as parameter.
    else:
        return "NO ID GIVEN TO DELETE" #If no ID parameter is given 
    delete_flight_sql = f"DELETE FROM flights WHERE id={id}" #Runs SQL statment using the id param as WHERE constraint. 
    execute_query(conn,delete_flight_sql) 

    return f" flight WITH ID:{id} DELETED" #Delete conformation


@app.route('/api/airport',methods=['POST']) #Adds new plane to plane table
def add_plane():
    request_data = request.get_json() #Allows data to added in JSON format
    new_id = request_data['id'] #planeid to add
    new_airportcode = request_data['airportcode'] #airportfrom to add
    new_airportname = request_data['airportname'] #airportto to add
    country = request_data['country']  #date to add 

    add_sql = f"INSERT INTO airport VALUES (id,'{new_id}','{new_airportcode}','{new_airportname}','{country}')"  #Turns JSON data to SQL insert
    execute_query(conn,add_sql)

    return "NEW airport ADDED"

    

user_result = [] #Holds all flight information
user_select = "SELECT id,planeid,airportfromid,airporttoid,date,Users.username,Users.password FROM flights JOIN Users ON Users.id = flight.userid" #SELECT statment for JOINed table
users = execute_read_query(conn,user_select) #Executes the query
for user in users:
        user_result.append(user) # Add the records to the user_results list
# print(user_result)
@app.route('/api/userpw',methods=['GET'])  #To test use Username:User1  and Password: Hello (case sensitive)
def user_trip():
    username = request.headers['username'] #Creates username header
    pw = request.headers['password'] #Creates password header
    hashedResult = hashlib.sha256(pw.encode()) #Allows hash to be decoded later on.
    for ur in user_result: #parses through user_results list
        if username == ur['username'] and hashedResult.hexdigest() == ur['password']: #Checks if user name and password match any of the users in the user table.
            user_trips_sql = f"""SELECT d.City,startdate,enddate,cost,Users.username,tripname,transportation FROM Trip JOIN Users ON Users.id = Trip.userid 
            JOIN Destination d on Trip.destinationid = d.id   
            WHERE Users.username ='{username}'""" #Selects the destination and trip tied to the user that logged  in.
            user_t_results = execute_read_query(conn,user_trips_sql)
            access_use = [] #Houses query result from line 177-180
            access_use.append(user_t_results) #Adds result to access_use
            return jsonify(access_use)
    return "ERROR" #if user name and id dont match
    
            
    
    
    
    



app.run()
