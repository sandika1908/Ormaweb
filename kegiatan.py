from flask import (render_template, request,
                   redirect, url_for, Blueprint)
import urllib.request
import json
from url import BASE_URL

kegiatan = Blueprint('kegiatan', __name__)

@kegiatan.route('/kegiatan')
def show_kegiatan():
    url = f"{BASE_URL}/ormaweb/api/v1/kegiatan/"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template('kegiatan.html', data=dict['results'])