from flask import Flask,request, jsonify
from flask_cors import CORS
from database import *
import sqlite3
import uuid

app = Flask(__name__)
CORS(app)


# Backend Routes
@app.route('/Cards', methods=['GET'])
def GetAllCards():
    conn = sqlite3.connect('Mydatabase.db')
    try:
        cards = FetchAllCards(conn)
        response = jsonify(cards)
        return response,200
    except Exception as e:  
        response = jsonify({"message":str(e)})
        return response,400

@app.route('/Users', methods=['GET'])
def GetAllUsers():
    conn = sqlite3.connect('Mydatabase.db')
    try:
        users = FetchAllUsers(conn)
        response = jsonify(users)
        return response,200
    except Exception as e:  
        response = jsonify({"message":str(e)})
        return response,400
              
@app.route('/create_card', methods=['POST'])
def CreateCard():
    conn = sqlite3.connect('Mydatabase.db')
    try:
        userid = request.json.get('userid')
        description = request.json.get('description')
        InsertCard(conn,userid,description)
        response = jsonify({"message":"Card created successfully"})
        return response,200
    except Exception as e:
        response = jsonify({"message":str(e)})
        return response,400

@app.route('/create_user', methods=['POST'])    
def CreateUser():
    conn = sqlite3.connect('Mydatabase.db')
    try:
        userid = str(uuid.uuid4())
        fullname = request.json.get('fullname')  
        role = request.json.get('role')
        InsertUser(conn,userid,fullname,role)
        response = jsonify({"message":"User created successfully","userid":userid})
        return response,200
    except Exception as e:
        response = jsonify({"message":str(e)})
        return response,400
    
@app.route("/Get_user",methods = ['GET'])
def GetUser():
    conn = sqlite3.connect('Mydatabase.db')
    try:
        userid = request.json.get("userid")
        user = FetchUser(conn,userid)
        response = jsonify({"userid":user[0],"FullName":user[1],"Role":user[2]})
        return response,200
    except Exception as e :
        response= jsonify({"message":f"Failed while retriving the user{userid}"})
        return response,400
    
@app.route("/Get_card",methods=['GET'])
def GetCard():
    conn = sqlite3.connect('Mydatabase.db')
    try:
        cardid = request.json.get("cardid")
        card = FetchCard(conn,cardid)
        response = jsonify({"cardid":card[0],"userid":card[1],"description":card[2]})
        return response,200
    except Exception as e :
        response= jsonify({"message":f"Failed while retriving the card{cardid}"})
        return response,400
        
@app.route("/delete_card", methods=['DELETE'])
def DeleteCard():
    conn = sqlite3.connect('Mydatabase.db')
    cursor = conn.cursor()
    cardid = request.json.get("cardid")
    try:
        cursor.execute('DELETE FROM Cards WHERE Cardid = ?', (cardid,))
        conn.commit()
        conn.close()
        response = jsonify({"message":"Card deleted successfully"})
        return response,200
    except Exception as e:
        response = jsonify({"message":str(e)})
        print(str(e))
        return response


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8888)
















