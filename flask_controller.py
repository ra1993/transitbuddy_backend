from flask import Flask, render_template, request, redirect, session, jsonify, flash, url_for
# from '/home/richarda/Bootcamp/project_MTA/backend_app/util.py' import encrypt_password

from backend_app.user import User
from flask_cors import CORS

dbpath = "./data/transit.db"

app = Flask(__name__)
CORS(app)

#homepage
@app.route('/')
@app.route('/homepage', methods=["GET"])
def homepage():
    pass


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

    new_user = User(pk = None, username = username, encrypted_password = encrypted_password, f_name = f_name, l_name = l_name, balance = balance)

    try:
        new_user.save()
        print("Thanks for joining Transit Buddy!", new_user.username)
    except:
        time.sleep(5)
        return jsonify({"error": error_message})
    finally: 
        #should return user to loggedin screen
        return redirect("/homepage")


# @app.route('/login', methods=["POST"])
# def login():

#     error_message = "Error: Invalid Credentials!"
#     data = request.get_json()
    
#     username = data['username']
#     password = data['password']
       
#         try:
#             user_account = User.login(username, password)
#             session['user_account'] = user_account.pk
#             print(user_account,"LOGIN SUCCESSFULLL>>>>>>>>>>>")
#         except:
#             if user_account == False:
#                 print("Invalid user credentials")
#                 return redirect("/login") #return to login
#         else:
            
#             return redirect("/loggedin_menu/", user_account = session)


if __name__ == "__main__":
    app.run(debug=True, port = 5000)