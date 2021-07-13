from flask import Blueprint

MM = Blueprint("MM", __name__,template_folder='./templates/')


@MM.route('/Main')
def index():
    return 'hellene'
