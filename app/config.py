import os


class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = 'yoursecretkey' #os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'screening.db')    #os.environ.get('SQLALCHEMY_DATABASE_URI')
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    JWT_SECRET_KEY = 'qaz'
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '5b604850cff72e'
    MAIL_PASSWORD = '8732de9e4f7a14'
    MAIL_USE_SSL = False
