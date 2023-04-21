import flask
from flask import jsonify
from flask import request
from sql import create_connection
from sql import execute_read_query
import creds

#setting up app name
app = flask.Flask(__name__)
app.config["DEBUG"] = True

snowboard = [
          {'id': 0,
           'boardtype': 'all_mountain',
           'brand': 'burton',
           'msrp': '499'
           'size': '20_inches'},
          {'id': 1,
           'boardtype': 'freestyle',
           'brand': 'solomon',
           'msrp': '599'
           'size': '25_inches'}
          {'id': 2,
           'boardtype': 'freeride',
           'brand': 'nidecker',
           'msrp': '699'
           'size': '21_inches'}
          {'id': 3,
           'boardtype': 'powder',
           'brand': 'lib_tech',
           'msrp': '299'
           'size': '24_inches'}
           {'id': 4,
           'boardtype': 'splitboard',
           'brand': 'arbor',
           'msrp': '399'
           'size': '29_inches'}
]

#default url
@app.route('/', methods=['GET'])
def api_all():
    return jsonify(snowboard)
  
#to get all the snowboards
@app.route('/api/snowboard', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id])
    else:
        return 'ERROR: No ID provided'
    results = []
    for id in snowboard:
        if snowboard['id'] == id:
             results.append(snowboard)
    return jsonify(results)
     
#to get a particular snowboard                              
@app.route('/api/snowboard', methods=['POST'])
def add_board():
    request_data = request.get_json()
    newid = request_data['id']
    newboardtype = request_data['boardtype']
    newbrand = request_data['brand']
    newmsrp = request_data['msrp']
    newsize = request_data['size']
     
    snowboard.append({'id': newid, 'boardtype': newboardtype, 'brand': newbrand, 'msrp': newmsrp, 'size': newsize})                          
                              
    return 'Add request was successful'
                              
 @app.route('/api/snowboardel, methods=['DELETE'])
 def delete_board():
     request_data = request.get_json()
     idToDelete = request_data['id']
     for i in range(len(snowboard)-1, -1, -1):
         if snowboard[i]['id'] == idToDelete:
            del(snowboard[i])
     return "Delete request succesful"
            
 
 @app.route('/api/snowboarduser', methods=['GET'])
 def api_users_id():
     if 'id' in request.args:
         id = int(request.args['id])
     else:
         return 'ERROR: No ID provided'
     myCreds = creds.Creds()
     conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
     sql = "SELECT * FROM users"
     users = execute_read_query(conn, sql)                          
     results = []
                               
     for user in users:
         if user['id'] == id:
             results.append(user)
         return jsonfiy(results)
                               
            
            
  app.run()          
            
