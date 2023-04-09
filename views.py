from app import app, current_user
# from models import db, User, Domain, PassiveNetworkData, BreachData, CustomerEmployeeInfo
from models import *
# from forms import
from flask import  Response, render_template, request, render_template_string, redirect
from flask import session, url_for
from flask_security import auth_required, roles_required



# Views
@app.route("/")
@auth_required()
def home():
    return render_template("index.html")





@app.route('/logout')  
@auth_required()
def logout():
    logout_user()
    return "Now logged out"



@app.route('/home', methods=['POST','GET'])
@auth_required()
def user():
    return render_template('home.html')


@app.route('/protected')
@auth_required()
@roles_required('admin')
def protected():
    return render_template('protected.html')



@app.route('/unprotected')
def unprotected():
    return render_template('unprotected.html')

