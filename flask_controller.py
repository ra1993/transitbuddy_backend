from flask import Flask, render_template, request, redirect, session, jsonify, flash, url_for
import requests
from user import User
from flask_cors import CORS

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

    encrypted_password = password

    new_user = User(username = username, encrypted_password = encrypted_password, f_name = f_name, l_name = l_name, email = email)

    try:
        new_user.save()
       
    except:
        time.sleep(5)
        return jsonify({"error": error_message})
    finally: 
      
        return jsonify({"Welecome": new_user.username})




if __name__ == "__main__":
    app.run(debug=True)

@app.route('/login', methods=["POST"])
def login():

    error_message = "Error: Invalid Credentials!"
    data = request.get_json()
    
    username = data['username']
    password = data['password']
       
        try:
            user_account = User.login(username, password)
            session['user_account'] = user_account.pk
            print(user_account,"LOGIN SUCCESSFULLL>>>>>>>>>>>")
        except:
            if user_account == False:
                print("Invalid user credentials")
                return redirect("/home") #return to login
        else:
            
            return jsonify({}) user_account = session)





# @app.route('/comment/<user_account>', methods=["GET"])
# def comment():



