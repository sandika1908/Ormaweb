from flask import (render_template, request,
                   redirect, url_for, Blueprint)
import urllib.request
import json
import requests
from url import BASE_URL

prestasi = Blueprint('prestasi',__name__)


@prestasi.route('/prestasi/<int:id_ormawa>')
def show_prestasi_by_id_ormawa(id_ormawa: int):
    url = f"{BASE_URL}/ormaweb/api/v1/prestasi/{id_ormawa}"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template("prestasi.html", data=dict['results'])


@prestasi.route('/tambah_prestasi/<int:id_ormawa>', methods=['POST'])
def tambah_prestasi(id_ormawa):
    url = f"{BASE_URL}/ormaweb/api/v1/prestasi/{id_ormawa}"

    data_send = request.form.to_dict()
    requests.post(url, json=data_send)
    print(dict)
    print(request.form.to_dict())
    return redirect(url_for('dashboard'))


@prestasi.route('/update_form_prestasi/<int:id_prestasi>/')
def update_form_prestasi(id_prestasi):
    url = f"{BASE_URL}/ormaweb/api/v1/prestasi_by_id/{id_prestasi}"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template('update_prestasi.html', data=dict)


@prestasi.route('/update_prestasi/<int:id_prestasi>/', methods=['POST'])
def update_prestasi(id_prestasi):
    url = f"{BASE_URL}/ormaweb/api/v1/prestasi/{id_prestasi}/"

    data_send = request.form.to_dict()
    requests.patch(url, json=data_send)
    print(dict)
    print(request.form.to_dict())
    return redirect(url_for('dashboard'))


@prestasi.route('/hapus_prestasi/<int:id_prestasi>', methods=['POST'])
def hapus_prestasi(id_prestasi):
    url = f"{BASE_URL}/ormaweb/api/v1/prestasi/{id_prestasi}"

    #data_send = request.form.to_dict()
    requests.delete(url)
    print(dict)
    print(request.form.to_dict())
    return redirect(url_for('dashboard'))