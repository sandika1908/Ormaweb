from flask import (render_template, request,
                   redirect, url_for, Blueprint)
import requests
import urllib.request
import json
from url import BASE_URL

admin = Blueprint('admin', __name__)


@admin.route('/admin')
def show_admin():
    url = f"{BASE_URL}/ormaweb/api/v1/admin/"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template('admin.html', data=dict['results'])


@admin.route('/admin/<int:id>', methods=['GET'])
def update_form_admin(id): 
    url = f"{BASE_URL}/ormaweb/api/v1/admin/{id}/"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template('update_users.html', data=dict)


@admin.route('/admin/<int:id>', methods=['POST'])
def update_admin(id):
    url = f"{BASE_URL}/ormaweb/api/v1/admin/{id}/"

    data_send = request.form.to_dict()
    requests.patch(url, json=data_send)
    print(dict)
    print(request.form.to_dict())
    return redirect(url_for('admin.show_admin'))


@admin.route('/tambah_admin', methods=['POST'])
def tambah_admin():
    url = f"{BASE_URL}/ormaweb/api/v1/admin/"

    data_send = request.form.to_dict()
    requests.post(url, json=data_send)
    print(dict)
    print(request.form.to_dict())

    return redirect(url_for('admin.show_admin'))
