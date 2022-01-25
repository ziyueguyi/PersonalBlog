from flask import Blueprint, render_template

MM = Blueprint("MainModule", __name__, template_folder='./templates', static_folder='./static',
               static_url_path='static')


@MM.route('/Main')
def index():
    return render_template('index.html')
