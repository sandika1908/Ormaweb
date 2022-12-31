from flask import (render_template, request,
                   redirect, url_for, Blueprint)
import urllib.request
import json
from url import BASE_URL

kegiatan = Blueprint('kegiatan', __name__)

@kegiatan.route('/ormawa')
def show_kegiatan():
    url = f"{BASE_URL}/ormaweb/api/v1/ormawa/"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template('dashboard.html', data=dict['results'])