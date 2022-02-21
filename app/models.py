from app import app
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os


with app.app_context():
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'screening.db')
    db = SQLAlchemy(app)
    ma = Marshmallow(app)


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
    test_user = User(first_name='test', last_name='test',
                     email='test@test.com', phone_number=9870157121, password='test')
    db.session.add(test_user)
    db.session.commit()
    print('Database Seeded!')


# Database Models
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(Integer)
    password = Column(String)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'password')


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


class VisitorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'password')


visitor_schema = VisitorSchema()
visitors_schema = VisitorSchema(many=True)