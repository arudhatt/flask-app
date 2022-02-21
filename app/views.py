from flask import render_template
from app import app


@app.route('/')
def home():
    return "<h1>Hello World<h1>"
    # return render_template('home.html')


@app.route('/not_found')
def not_found():
    return "<h2>Page Not Found<h2>"
    # return render_template('other.html')