from flask import (render_template, request, session,
                   redirect, url_for, Blueprint)
import urllib.request
import json
import requests
from url import BASE_URL
import os

ormawa = Blueprint('ormawa', __name__)


@ormawa.route('/ormawa')
def show_ormawa():
    url = f"{BASE_URL}/ormaweb/api/v1/ormawa/"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template('ormawa.html', data=dict['results'])


@ormawa.route('/ormawa/<int:id_ormawa>')
def show_ormawa_by_id(id_ormawa):
    url = f"{BASE_URL}/ormaweb/api/v1/ormawa/{id_ormawa}"
    url_kegiatan = f"{BASE_URL}/ormaweb/api/v1/kegiatan/{id_ormawa}"

    response = urllib.request.urlopen(url)
    response_kegiatan = urllib.request.urlopen(url_kegiatan)

    data_kegiatan = response_kegiatan.read()
    data = response.read()

    dict_kegiatan = json.loads(data_kegiatan)
    dict = json.loads(data)

    return render_template('csc.html', data=dict, kegiatan=dict_kegiatan['results'])


@ormawa.route('/update_form_ormawa/<int:id_ormawa>/')
def update_form_ormawa(id_ormawa):
    url = f"{BASE_URL}/ormaweb/api/v1/ormawa/{id_ormawa}"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template('update_ormawa.html', data=dict)


@ormawa.route('/update_rmawa/<string:alamat_gambar>/<int:id_ormawa>/', methods=['POST'])
def update_ormawa(id_ormawa, alamat_gambar):
    url = f"{BASE_URL}/ormaweb/api/v1/ormawa/{id_ormawa}"

    data_send = request.form.to_dict()
    file = request.files['file']
    print(file.filename)
    print(alamat_gambar)
    if file.filename:
        data_send['alamat_gambar'] = file.filename
        file.save(os.path.join('static/images', file.filename))

    else:
        data_send['alamat_gambar'] = alamat_gambar

    requests.patch(url, json=data_send)
    print(data_send)
    return redirect(url_for('dashboard'))


@ormawa.route('/tambah_ormawa', methods=['POST'])
def tambah_ormawa():
    url = f"{BASE_URL}/ormaweb/api/v1/ormawa/"

    data_send = request.form.to_dict()
    file = request.files['file']
    data_send['alamat_gambar'] = file.filename
    if session['username'] == '':
        print('login terlebih dahulu')
        return redirect(url_for('auth.login'))
    else:
        requests.post(url, json=data_send)
        file.save(os.path.join('static/images', file.filename))
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
