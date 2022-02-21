from app import app
from flask import jsonify, request
from app import models, views
from flask_jwt_extended import JWTManager, create_access_token
from flask_mail import Mail, Message


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


@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    test = models.User.query.filter_by(email=email).first()
    if test:
        return jsonify(message='That email already exists.'), 409
    else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        password = request.form['password']
        user = models.User(first_name=first_name, last_name=last_name, email=email,
                           phone_number=phone_number, password=password)
        models.db.session.add(user)
        models.db.session.commit()
        return jsonify(message='User Added!'), 201


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
