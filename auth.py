from flask import (render_template, request,
                   redirect, url_for, Blueprint, session)

import requests
from url import BASE_URL

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_data = request.form.to_dict()
        url = f"{BASE_URL}/ormaweb/api/v1/auth/login"
        request_login = requests.post(url, json=user_data)
        print(request.form.to_dict())

        if request_login.status_code == 200:
            print(request_login.json())
            response_data = request_login.json()
            session['logged_in'] = True
            session['id'] = response_data['id']
            session['username'] = response_data['ormawa']
            session['role'] = response_data['role']
            
            return redirect(url_for('dashboard'))
    return render_template('login.html')
        
@auth.route('/logout/')
def logout():
    session.pop('username', None)
    session.pop('logged_in', None)
    session.pop('id', None)
    session.pop('role', None)

    print('berhasil logout')
    return redirect(url_for('login'))