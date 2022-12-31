from flask import Flask, render_template, url_for, redirect, flash, session, jsonify
from flask import request
import mysql.connector
import werkzeug
import urllib.request, json 
from url import BASE_URL

from ormawa import ormawa
from admin import admin

application = Flask(__name__)

application.register_blueprint(ormawa)
application.register_blueprint(admin)

@application.route('/')
@application.route('/index')
def index():
    url = f"{BASE_URL}/ormaweb/api/v1/ormawa/"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("index.html", data=dict['results'])

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

@application.route('/kegiatan')
def kegiatan():
    return render_template("kegiatan.html")

if __name__ == '__main__':
    application.run(debug=True)