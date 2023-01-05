from flask import (render_template, request,
                   redirect, url_for, Blueprint)
import urllib.request
import json
import requests
from url import BASE_URL

ormawa = Blueprint('ormawa', __name__)


@ormawa.route('/ormawa')
def show_ormawa():
    url = f"{BASE_URL}/ormaweb/api/v1/ormawa/"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template('ormawa.html', data=dict['results'])


@ormawa.route('/update_form_ormawa/<int:id_ormawa>/')
def update_form_ormawa(id_ormawa):
    url = f"{BASE_URL}/ormaweb/api/v1/ormawa/{id_ormawa}"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template('update_ormawa.html', data=dict)


@ormawa.route('/update_rmawa/<int:id_ormawa>/', methods=['POST'])
def update_ormawa(id_ormawa):
    url = f"{BASE_URL}/ormaweb/api/v1/ormawa/{id_ormawa}"

    data_send = request.form.to_dict()
    requests.patch(url, json=data_send)
    print(dict)
    print(request.form.to_dict())
    return redirect(url_for('dashboard'))


@ormawa.route('/tambah_ormawa', methods=['POST'])
def tambah_ormawa():
    url = f"{BASE_URL}/ormaweb/api/v1/ormawa/"

    data_send = request.form.to_dict()
    requests.post(url, json=data_send)
    print(dict)
    print(request.form.to_dict())
    return redirect(url_for('dashboard'))


@ormawa.route('/hapus_ormawa/<int:id_ormawa>', methods=['POST'])
def hapus_ormawa(id_ormawa):
    url = f"{BASE_URL}/ormaweb/api/v1/ormawa/{id_ormawa}"

    data_send = request.form.to_dict()
    requests.delete(url)
    print(dict)
    print(request.form.to_dict())
    return redirect(url_for('dashboard'))
