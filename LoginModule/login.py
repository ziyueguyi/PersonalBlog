from config import STATE_CODE
from LoginModule import model as md
from PublicFunction.db_connect import db
from PublicFunction.token import create_token
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash

LoginModule = Blueprint("LoginModule", __name__, template_folder='./templates', static_folder='./static',
                        static_url_path='static')


@LoginModule.route('/', methods=['GET', 'POST'])
def index():
    """
    返回登录页面
    :return:
    """
    return render_template('index.html')


@LoginModule.route('/ver_inf', methods=['POST'])
def ver_inf():
    o_token = None
    try:
        name = request.form.get('login')
        pwd = request.form.get('pwd')
        code = request.form.get('code')
        if code:
            user = md.Users
            user = db.session.query(user.id).filter(user.a_name == name and user.password == pwd).first()
            if user:
                cd = 200
                o_token = create_token(user[0])
            else:
                cd = 4002
        else:
            cd = 4003
    except BaseException as e:
        print('{0}'.format(e))
        cd = 4004
    sc = STATE_CODE[cd]
    return jsonify(code=sc['code'], msg=sc['msg'], token=o_token)
