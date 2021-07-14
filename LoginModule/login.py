from config import state_code

from flask import Blueprint, render_template, request, jsonify, g
from LoginModule import model as md
from PublicFunction.db_connect import db
# from PublicFunction.token import create_token, generate_auth_token, auth

LoginModule = Blueprint("LoginModule", __name__, template_folder='./templates', static_folder='./static',
                        static_url_path='static')


@LoginModule.route('/index')
def index():
    """
    返回登录页面
    :return:
    """
    return render_template('index.html')


# @LoginModule.route('/ver_inf', methods=['POST'])
# @auth.login_required
# def ver_inf():
#     token = generate_auth_token(g.user_id)
#     cd = 200
#     sc = state_code[cd]
#     sc['token'] = token
#     return jsonify(sc)


@LoginModule.route('/ver_inf', methods=['POST'])
def ver_inf():
    o_token = None
    try:
        name = request.form.get('login')
        pwd = request.form.get('pwd')
        code = request.form.get('code')
        if code:
            user = md.Users
            user = db.session.query(user.id, user.password).filter(user.a_name == name).all()
            if len(user):
                if pwd == user[0][1]:
                    cd = 200
                    # o_token = create_token(user[0][0])
                    sc = state_code[cd]
                    print(1)
                    return jsonify(code=sc['code'], msg=sc['msg'], data=o_token)
                else:
                    cd = 4001
            else:
                cd = 4002
        else:
            cd = 4003
    except BaseException as e:
        ''.format(e)
        cd = 4004
    sc = state_code[cd]
    return jsonify(code=sc['code'], msg=sc['msg'], data=o_token)
