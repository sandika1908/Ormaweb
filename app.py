from flask import Flask, render_template, url_for, redirect, flash, session, jsonify
from flask import request
#import mysql.connector
import werkzeug
import urllib.request, json 
from url import BASE_URL

from ormawa import ormawa
from admin import admin
from auth import auth

application = Flask(__name__)

application.secret_key = '1768b67767bb8ac8f5b7ecdb48dbef720703387ccce086c562a4bf61000f9c31'

application.register_blueprint(ormawa)
application.register_blueprint(admin)
application.register_blueprint(auth)

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


@application.route('/create_prestasi')
def create_prestasi():
    return render_template("create_prestasi.html")

@application.route('/create_kegiatan')
def create_kegiatan():
    return render_template("create_kegiatan.html")

@application.route('/update_ormawa')
def update_ormawa():
    return render_template("update_ormawa.html")

@application.route('/update_prestasi')
def update_prestasi():
    return render_template("update_prestasi.html")

@application.route('/update_kegiatan')
def update_kegiatan():
    return render_template("update_kegiatan.html")

@application.route('/galeri')
def galeri():
    return render_template("galeri.html")

@application.route('/create_ormawa')
def create_ormawa():
    return render_template("create_ormawa.html")

@application.route('/create_users')
def create_users():
    url = f"{BASE_URL}/ormaweb/api/v1/ormawa/"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    
    return render_template("create_users.html", result =dict['results'])

@application.route('/create_galeri')
def create_galeri():
    return render_template("create_galeri.html")

if __name__ == '__main__':
    application.run(debug=True)