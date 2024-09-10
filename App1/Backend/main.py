# pip install Flask
# pip install flask-cors

from flask import request, jsonify,Flask
from flask_cors import CORS 
from utils import  Fetch_All_Contacts,Insert_Contact,Update_contact,Fetch_Contact,Delete_Contact
import sqlite3


app = Flask(__name__)
CORS(app)


@app.route('/contacts', methods=['GET']) 
def Get_Contacts():
    conn = sqlite3.connect('database.db')
    Contacts = Fetch_All_Contacts(conn)
    response = jsonify({"contacts":Contacts})  
    #print(type(response)) #flask.Response
    return response

@app.route('/contact/<int:id>', methods=['GET'])
def Get_Contact(id):
    conn = sqlite3.connect('database.db')
    contact = Fetch_Contact(conn,id) # tuple
    if contact:
        response = jsonify({"contact":contact})
        return response,202
    
    return jsonify({"message":"Contact not found"}), 404

@app.route("/create", methods=['POST'])
def Create_Contact():
    # Tha data sent with the request
    
    firstName = request.json.get('firstName')
    lastName = request.json.get('lastName')
    isStudent = request.json.get('isStudent')
    email     = request.json.get('email')
    
    # We can check if all data was sent
    if firstName and lastName:
        conn = sqlite3.connect('database.db')
        Insert_Contact(conn, firstName, lastName,isStudent, email)
        response = jsonify({"message":"Contact created successfully"})
        return response,200
    
    response = jsonify({"message":"You must send firstName, lastName"})
    return response,400

@app.route("/update/<int:id>", methods=['PATCH']) 
def Update_Contact(id):
    conn = sqlite3.connect('database.db')
    contact = Fetch_Contact(conn,id) # tuple
    
    NewfirstName = request.json.get('firstName',contact[1])
    NewlastName = request.json.get('lastName',contact[2])
    NewIsStudent = request.json.get('isStudent',contact[3])
    Newemail = request.json.get('email',contact[4])
    try:
        Update_contact(conn, id,NewfirstName, NewlastName,NewIsStudent, Newemail)
        response = jsonify({"message":"Contact updated successfully"})
    except Exception as e:
        response = jsonify({"message":str(e)})

    return response
  
@app.route("/delete/<int:id>", methods=['DELETE'])
def drop_Contact(id):
    conn = sqlite3.connect('database.db')
    contact = Fetch_Contact(conn,id) # tuple
    if  contact:
        try:
            conn = sqlite3.connect('database.db')
            Delete_Contact(conn, id)
            response = jsonify({"message":"Contact deleted successfully"})
            return response,200
        except Exception as e:
            response = jsonify({"message":str(e)})
            return response,400
    return jsonify({"message":"Contact not found"}),404

       
def run():
    app.run(debug=True)
    


run()

















