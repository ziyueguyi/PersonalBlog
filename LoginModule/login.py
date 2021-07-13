import json
import os

from flask import Blueprint, render_template, request
from LoginModule import model as md
from PublicFunction.db_connect import db

LoginModule = Blueprint("LoginModule", __name__, template_folder='./templates', static_folder='./static',
                        static_url_path='static')


@LoginModule.route('/index')
def index():
    """
    返回登录页面
    :return:
    """
    return render_template('index.html')


@LoginModule.route('/ver_inf', methods=['POST'])
def ver_inf():
    name = request.form.get('login')
    pwd = request.form.get('pwd')
    code = request.form.get('code')
    if code:
        user = md.Users
        user = db.session.query(user.password).filter(user.a_name == name).all()
        if len(user):
            if pwd == user[0][0]:
                code_dict = {'code': 200, 'text': '登录成功'}
            else:
                code_dict = {'code': 200, 'text': '密码错误'}
        else:
            code_dict = {'code': 200, 'text': '账号错误'}
    else:
        code_dict = {'code': 200, 'text': '验证码错误'}
    return json.dumps(code_dict, ensure_ascii=False)
