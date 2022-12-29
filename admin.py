from flask import (render_template, request,
                   redirect, url_for, Blueprint)
import urllib.request
import json
from url import BASE_URL

admin = Blueprint('admin', __name__)


@admin.route('/admin')
def show_admin():

    return render_template('admin.html')
