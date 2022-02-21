from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'screening.db')

db = SQLAlchemy(app)


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database Created')


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database Destroyed')


@app.cli.command('db_seed')
def db_seed():
    test_user = User(user_name='test', email='test@test.com', phone=9870157121, password='test')
    db.session.add(test_user)
    db.session.commit()
    print('Database Seeded!')


# Database Models
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(Integer)
    password = Column(String)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_name', 'email', 'phone_number', 'password')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class Visitor(db.Model):
    __tablename__ = 'visitors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(Integer)
    password = Column(String)
