from flask import Blueprint

MM = Blueprint("MM", __name__)


@MM.route('/')
def index():
    return 'hellene'
