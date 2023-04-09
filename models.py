from flask_security.models import fsqla_v2 as fsqla
from flask_security import SQLAlchemyUserDatastore, auth_required, Security
from flask_sqlalchemy import SQLAlchemy 

from app import app

from database import db


fsqla.FsModels.set_db_info(db)


# roles_users = db.Table('roles_users',
#         db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
#         db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, fsqla.FsRoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    

class User(db.Model, fsqla.FsUserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    # username = db.Column(db.String(50),nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship(
        'Role', secondary='roles_users', backref=db.backref('users', lazy='dynamic'))


class TestTable1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False) 
    entry_date = db.Column(db.Date, nullable=False)



class TestTable2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, foreign_key('User.id'))
    user_id = db.Column(db.String(50), nullable=False)
    some_column = db.Column(db.String(50), nullable=False)
    some_column2 = db.Column(db.Integer)
    entry_date = db.Column(db.Date, nullable=False)



user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

