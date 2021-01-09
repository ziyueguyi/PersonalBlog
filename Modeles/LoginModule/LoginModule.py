from flask import Blueprint, render_template
from Modeles.LoginModule import model

LM = Blueprint("LM", __name__, template_folder='templates', url_prefix='/LoginModule', static_url_path='static')


@LM.route('/index/')
def index():
    print(LM.jinja_loader)
    return render_template('index.html')
