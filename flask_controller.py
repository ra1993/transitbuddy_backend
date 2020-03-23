from flask import Flask, render_template, request, redirect, session, jsonify, flash, url_for
import requests
from user import User
from comment import Comment
from flask_cors import CORS
from util import get_stations
from util import encrypt_password
from util import get_stop_id

dbpath = "./data/transit.db"

app = Flask(__name__)
CORS(app)


with open("/home/richarda/apikeys/mtapikey","r") as file_object:
    api_key = file_object.readline().strip()

with open("/home/richarda/apikeys/weatherkey","r") as file_object:
    weather_key = file_object.readline().strip()


#homepage
# @app.route('/')
# @app.route('/homepage', methods=["GET"])
# def homepage():
#     pass

@app.route('/register', methods = ["POST"])
def register():

    error_message = "There was an error creating your account! Please try again."
    
    # f_name = request.get_json()['f_name']
    # l_name = request.get_json()['l_name']
    # username = request.get_json()['username']
    # password = request.get_json()['password']
    # email = request.get_json()['email']

    data = request.get_json()
    f_name = data['f_name']
    l_name = data['l_name']
    username = data['username']
    password = data['password']
    email = data['email']

    encrypted_password = encrypt_password(password)

    new_user = User(username = username, encrypted_password = encrypted_password, f_name = f_name, l_name = l_name, email = email)

    try:
        new_user.save()
       
    except:
        time.sleep(5)
        return jsonify({"error": error_message})
    finally: 
      
        return jsonify({"Thank You:": new_user.username})


@app.route('/login', methods=["POST"])
def login():

    error_message = "Error: Invalid Credentials!"
    successful = "Login Successful!"
    data = request.get_json()
    
    username = data['username']
    password = data['password']
    
    try:
        user_account = User.login(username, password)
    except:
        if user_account == False:
            return jsonify({"error": error_message}) #return to login
    else:
        
        return jsonify({"Welcome": user_account.username})

#------------------------------------------train,station and times
@app.route('/train/<letter>', methods =["POST", "GET"])
def get_train_stations(letter):

    if request.method == "POST":
        stations = get_stations(letter)
    # print(stations)

    if request.method == "GET":
        return ({"stations": stations})
    return ({"stations": stations})
    

@app.route('/incoming/time', methods = ["GET"])
def time():

    return jsonify({"incoming_time": "time"})

#-----------------------------------------------for user feeds and comment components
@app.route ('/comment', methods = ["POST"])
def comment():

    data = request.get_json()
    new_comment = Comment()

    return jsonify({"comment": "made a comment!"})

@app.route('/feed', methods = ["GET"])
def feed():
    pass

#----------------------------------------------get weather
@app.route('/weather', methods = ["GET"])
def weather_location():
    pass

if __name__ == "__main__":
    app.run(debug=True)
