import os
import json
from datetime import datetime
from collections import Counter
from functools import wraps
from datetime import datetime, timedelta
from warnings import filterwarnings

from flask import Flask, Response, render_template, request, render_template_string
from flask_security import  current_user, auth_required, roles_required, UserMixin, RoleMixin, hash_password
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

from sqlalchemy import desc, func, update


# from customforms import ExtendedRegisterForm

# apt installs:
# apt install python3-pymysql




# export FLASK_ENV=development

# create test user in python shell:
# from app import db, User
# from app import create_app

# testy = User(username="testy")
# app = create_app()
# with app.app_context:
#     db.session.add(testy)
#     db.session.commit()





### Initiate APP

# def create_app():
app=Flask(__name__)
app.config['DEBUG'] = True
# CHANGE THESE
# TODO
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", 'pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw')
app.config['SECURITY_PASSWORD_SALT'] = os.environ.get("SECURITY_PASSWORD_SALT", '146585145368132386173505678016728509634')


app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://testuser:Passw0rd@127.0.0.1/testdb'
# app.config['SQLALCHEMY_BINDS']={'extra_db':'mysql+pymysql://someuser:Passw0rd@127.0.0.1/extra_db','extra_db2':'mysql+pymysql://someuser:Passw0rd@localhost/extra_db2'}

#SETUP:

#SETUP:
# sudo mysql -e "create database users;create database testdb;CREATE USER testuser IDENTIFIED BY 'Passw0rd';select user from mysql.user;grant create, alter, update, delete, insert, select, references on testdb.* to testuser;"


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
#     "pool_pre_ping": True,
# }

app.config['SECURITY_POST_LOGOUT_VIEW'] = "/login"
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False
# app.config['SECURITY_RECOVERABLE'] = True
# app.config['SECURITY_CHANGEABLE'] = True
# app.config['SECURITY_EMAIL_SENDER'] = 'user@email.com'
# app.config['SECURITY_EMAIL_SUBJECT_REGISTER'] = 'This is a custom welcome title'
# app.config['SECURITY_EMAIL_PLAINTEXT'] = True
# app.config['SECURITY_EMAIL_HTML'] = False
# app.config.from_pyfile('mail_config.cfg')




from views import *
from database import db
migrate = Migrate(app, db)



db.init_app(app)


@app.before_first_request
def create_user():
    from models import user_datastore
    db.create_all()
    if not user_datastore.find_user(email="test@me.com"):
        user_datastore.create_user(email="test@me.com", password=hash_password("password"))
    db.session.commit()






