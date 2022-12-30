from flask import Flask, render_template, url_for, redirect, flash, session, jsonify
from flask import request
import mysql.connector
import werkzeug
import urllib.request, json 

from ormawa import ormawa
from admin import admin
from auth import auth

application = Flask(__name__)

application.secret_key = 'c24bf80e37ea94aa012725bfce23ca7603f9391031775d6b5886f25e133ab7dd'


application.register_blueprint(ormawa)
application.register_blueprint(admin)
application.register_blueprint(auth)

@application.route('/')
@application.route('/index')
def index():
    return render_template("index.html")

@application.route('/csc')
def csc():
    return render_template("csc.html")

@application.route('/login')
def login():
    return render_template("login.html")

@application.route('/register')
def register():
    return render_template("register.html")

@application.route('/dashboard')
def dashboard():
    return redirect(url_for('ormawa.show_ormawa'))

@application.route('/prestasi')
def prestasi():
    return render_template("prestasi.html")

if __name__ == '__main__':
    application.run(debug=True)