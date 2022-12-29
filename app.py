from flask import Flask, render_template, url_for, redirect, flash, session, jsonify
from flask import request
import mysql.connector
import werkzeug
import urllib.request, json 

application = Flask(__name__)

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
    return render_template("dashboard.html")

@application.route('/prestasi')
def prestasi():
    return render_template("prestasi.html")

if __name__ == '__main__':
    application.run(debug=True)