from flask import Blueprint

LM = Blueprint("LM", __name__)


@LM.route('/index')
def index():
    return 'hello'
