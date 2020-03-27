from flask import Flask, render_template, request, redirect, session, jsonify, flash, url_for
import requests
import datetime
#modules
from user import User
from comment import Comment
from flask_cors import CORS

#functions
from util import get_stations
from util import encrypt_password
from util import get_stop_id
from mta import get_train_time


dbpath = "./data/transit.db"
table3 = "comment"

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
    
    data = request.get_json()
    f_name = data['f_name']
    l_name = data['l_name']
    username = data['username']
    password = data['password']
    email = data['email']
    

    encrypted_password = encrypt_password(password)

    new_user = User(username = username, encrypted_password = encrypted_password, f_name = f_name, l_name = l_name, email = email, token = "")

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

    user_account = User.login(username, password)
    user_account.get_token() #creates token when user logs in
   
    if user_account == False:
        return jsonify({"error": error_message}) #return to login
    else:
 
        return jsonify({"token": user_account.token})

@app.route('/token/<token>', methods = ["GET"])
def token_auth(token):
    user_account = User.select_token(f"""WHERE token =?""", (token,))
    user_account = {
        "pk" : user_account.pk,
        "username" : user_account.username,
        "f_name" : user_account.f_name,
        "l_name" : user_account.l_name,
        "token" : user_account.token
    }
    return jsonify({"userData": user_account})

@app.route('/logout', methods = ["POST"])
def logout():
    data = request.get_json()
    user_account = User.select_one(f"""WHERE pk = ?""", (data["pk"],))
    user_account.del_token()
    return jsonify({"response": "Logged out successfully!"})

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
def get_time():
    
    return jsonify({"incoming_time": "time"})

#-----------------------------------------------for user feeds and comment components
@app.route ('/add/comment', methods = ["POST"])
def add_comment():
    data = request.get_json()
    time = strftime(datetime.datetime.now())
    comment = data['comment']
    new_comment = Comment(comment = comment, time = time)

    return jsonify({"comment": "made a comment!"})


@app.route('/view/comments')
def view_comments():
   #sql statement select all to pull all comments from table db based on user
   pass

@app.route('/feed', methods = ["GET"])
def feed():
    pass

#----------------------------------------------get weather
@app.route('/weather', methods = ["GET"])
def weather_location():
    pass

if __name__ == "__main__":
    app.run(debug=True)
