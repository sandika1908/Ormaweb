from flask import (render_template, request,
                   redirect, url_for, Blueprint)
import urllib.request
import json
from url import BASE_URL
import requests
import os

galeri = Blueprint('galeri', __name__)


@galeri.route('/galeri/<int:id_ormawa>')
def show_galeri(id_ormawa):
    url = f"{BASE_URL}/ormaweb/api/v1/galeri/{id_ormawa}"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template('galeri.html', data=dict['results'])


@galeri.route('/tambah_galeri/<int:id_ormawa>', methods=['POST'])
def tambah_galeri(id_ormawa):
    url = f"{BASE_URL}/ormaweb/api/v1/galeri/{id_ormawa}"
    file = request.files['file']
    data_send = {
        'alamat': file.filename
    }
    file.save(os.path.join('static/images', file.filename))
    requests.post(url, json=data_send)
    print(dict)
    print(request.form.to_dict())
    return redirect(url_for('dashboard'))


@galeri.route('/update_galeri/<int:id_gambar>/', methods=['POST'])
def update_gambar(id_gambar):
    url = f"{BASE_URL}/ormaweb/api/v1/galeri/{id_gambar}/"

    file = request.files['file']
    data_send = {
        'alamat': file.filename
    }
    file.save(os.path.join('static/images', file.filename))
    print(data_send)
    requests.patch(url, json=data_send)
    return redirect(url_for('dashboard'))

@galeri.route('/delete_galeri/<int:id_gambar>/', methods=['POST'])
def delete_gambar(id_gambar):
    url = f"{BASE_URL}/ormaweb/api/v1/galeri/{id_gambar}"

    requests.delete(url)
    return redirect(url_for('dashboard'))