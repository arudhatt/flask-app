from flask import Flask

app = Flask(__name__)

from app import views
from app import models
from app import user_views