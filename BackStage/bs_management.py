from flask import Blueprint, render_template, request, jsonify, make_response
from flask.views import MethodView

from LoginModule import model as lm_model
from BackStage import model as bs_model
from PublicFunction.token import verify_auth_token

BackStage = Blueprint("BackStage", __name__, template_folder='./templates', static_folder='./static',
                      static_url_path='static')


@BackStage.route('/', methods=['GET', 'POST'])
def index():
    """
    返回登录页面
    :return:
    """

    response = make_response(render_template('pb_index.html', foo=42))
    return response


# @BackStage.route('/get_user', methods=['GET', 'PosT'])
# # @login_required
# def get_user():
#     token = request.headers.get('z-token', None)
#     ver_token = verify_auth_token(token)
#
#     name_p = None
#     mailbox_p = None
#     if ver_token:
#         number_id = ver_token
#         try:
#             user = model.Users
#             users = user.query.filter(user.id == number_id).first()
#             name_p = users.ui[0].name
#             mailbox_p = users.ui[0].mailbox
#         except BaseException as e:
#             print(e)
#     return jsonify(name=name_p, mailbox=mailbox_p)


@BackStage.route('/res_manage', methods=['GET', 'POST'])
# @login_required
def resource_manage():
    """
        返回登录页面
        :return:
        """
    return render_template('pb_index.html')


@BackStage.route('/pass_manage', methods=['GET', 'POST'])
# @login_required
def password_manage():
    """
        返回登录页面
        :return:
        """

    return render_template('pb_index.html')


@BackStage.route('/user_manage', methods=['GET', 'POST'])
# @login_required
def user_manage():
    """
        返回登录页面
        :return:
        """

    return render_template('pb_index.html')


@BackStage.route('/aut_manage', methods=['GET', 'POST'])
# @login_required
def authority_manage():
    """
        返回登录页面
        :return:
        """
    return render_template('pb_index.html')


# @BackStage.route('/get_user', methods=['GET', 'PosT'])
# @login_required
class Get_User(MethodView):
    @staticmethod
    def get():
        token = request.headers.get('z-token', None)
        ver_token = verify_auth_token(token)

        name_p = None
        mailbox_p = None
        if ver_token:
            number_id = ver_token
            try:
                user = lm_model.Users
                users = user.query.filter(user.id == number_id).first()
                name_p = users.ui[0].name
                mailbox_p = users.ui[0].mailbox
            except BaseException as e:
                print(e)
        return jsonify(name=name_p, mailbox=mailbox_p)


def register_api():
    # get_user = Get_User.as_view('get_user')
    BackStage.add_url_rule('/get_user', view_func=Get_User.as_view('get_user'), methods=['GET', ])


register_api()
