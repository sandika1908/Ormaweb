from flask import (render_template, request,
                   redirect, url_for, Blueprint)
import urllib.request
import json
from url import BASE_URL

prestasi = Blueprint('prestasi', __name__)

@prestasi.route('/prestasi/<int:id_ormawa>')
def show_prestasi_by_id_ormawa(id_ormawa: int):
    url = f"{BASE_URL}/ormaweb/api/v1/prestasi/{id_ormawa}"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template("prestasi.html", data=dict['results'])