from app import app
from flask import jsonify, request
from app import models
from flask_jwt_extended import JWTManager, create_access_token
from flask_mail import Mail, Message
import re

app.config['JWT_SECRET_KEY'] = 'qaz'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
# app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
# app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_USERNAME'] = '5b604850cff72e'
app.config['MAIL_PASSWORD'] = '8732de9e4f7a14'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

jwt = JWTManager(app)
mail = Mail(app)


# Method for user registeration
@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    test = models.User.query.filter_by(email=email).first()
    if test:
        return jsonify(message='That email already exists.'), 409
    else:
        password = request.form['password']
        password_strength = password_check(password)
        if not password_strength['password_ok']:
            return password_strength
        else:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            phone_number = request.form['phone_number']
            user = models.User(first_name=first_name, last_name=last_name, email=email,
                           phone_number=phone_number, password=password)
            models.db.session.add(user)
            models.db.session.commit()
            return jsonify(message='User Added!'), 201


# Method for User Login
@app.route('/login', methods=['POST'])
def login():
    if request.is_json:
        email = request.json['email']
        password = request.json['password']
    else:
        email = request.form['email']
        password = request.form['password']
    user = models.User.query.filter_by(email=email, password=password).first()
    if user:
        access_token = create_access_token(identity=email)
        return jsonify(message='Login Successful!', access_token=access_token)
    else:
        return jsonify(message='Bad email or password!'), 401


# Method to retrieve forgotten password
@app.route('/retrieve_password/<string:email>', methods=['GET'])
def retrieve_password(email: str):
    user = models.User.query.filter_by(email=email).first()
    if user:
        msg = Message("Your screening app password is: " + user.password,
                      sender="admin@planetaryapi.com",
                      recipients=[email])
        mail.send(msg)
        return jsonify(message='Password sent to ' + email)
    else:
        return jsonify(message='That email does not exist.'), 401


# Method to check password restrictions.
def password_check(password):
    """
    Verify the strength of 'password'
    Returns a dict indicating the wrong criteria
    A password is considered strong if:
        8 characters length or more
        1 digit or more
        1 symbol or more
        1 uppercase letter or more
        1 lowercase letter or more
    """

    # calculating the length
    length_error = len(password) < 8

    # searching for digits
    digit_error = re.search(r"\d", password) is None

    # searching for uppercase
    uppercase_error = re.search(r"[A-Z]", password) is None

    # searching for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None

    # searching for symbols
    symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None

    # overall result
    password_ok = not ( length_error or digit_error or uppercase_error or lowercase_error or symbol_error )

    return {
        'password_ok' : password_ok,
        'length_error' : length_error,
        'digit_error' : digit_error,
        'uppercase_error' : uppercase_error,
        'lowercase_error' : lowercase_error,
        'symbol_error' : symbol_error,
    }

