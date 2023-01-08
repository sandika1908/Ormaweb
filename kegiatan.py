from flask import (render_template, request,
                   redirect, url_for, Blueprint)
import urllib.request
import json
from url import BASE_URL
import requests

kegiatan = Blueprint('kegiatan', __name__)


@kegiatan.route('/kegiatan/<int:id_ormawa>')
def show_kegiatan(id_ormawa):
    url = f"{BASE_URL}/ormaweb/api/v1/kegiatan/{id_ormawa}"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template('kegiatan.html', data=dict['results'])


@kegiatan.route('/tambah_kegiatan/<int:id_ormawa>', methods=['POST'])
def tambah_kegiatan(id_ormawa):
    url = f"{BASE_URL}/ormaweb/api/v1/kegiatan/{id_ormawa}"

    data_send = request.form.to_dict()
    requests.post(url, json=data_send)
    print(dict)
    print(request.form.to_dict())
    return redirect(url_for('dashboard'))


@kegiatan.route('/update_form_kegiatan/<int:id_kegiatan>/')
def update_form_kegiatan(id_kegiatan):
    url = f"{BASE_URL}/ormaweb/api/v1/kegiatan_by_id/{id_kegiatan}"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template('update_kegiatan.html', data=dict)


@kegiatan.route('/update_kegiatan/<int:id_kegiatan>/', methods=['POST'])
def update_kegiatan(id_kegiatan):
    url = f"{BASE_URL}/ormaweb/api/v1/kegiatan/{id_kegiatan}/"

    data_send = request.form.to_dict()
    requests.patch(url, json=data_send)
    print(dict)
    print(request.form.to_dict())
    return redirect(url_for('dashboard'))

@kegiatan.route('/hapus_kegiatan/<int:id_kegiatan>', methods=['POST'])
def hapus_kegiatan(id_kegiatan):
    url = f"{BASE_URL}/ormaweb/api/v1/kegiatan/{id_kegiatan}"

    #data_send = request.form.to_dict()
    requests.delete(url)
    print(dict)
    print(request.form.to_dict())
    return redirect(url_for('dashboard'))
