from flask import (render_template, request,
                   redirect, url_for, Blueprint)
import urllib.request
import json
from url import BASE_URL

ormawa = Blueprint('ormawa', __name__)

@ormawa.route('/ormawa')
def show_ormawa():
    url = f"{BASE_URL}/ormaweb/api/v1/ormawa/"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template('dashboard.html', data=dict['results'])