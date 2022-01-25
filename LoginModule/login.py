from flask.views import MethodView

from PublicFunction.public_func import r_code
from LoginModule import model as md
from PublicFunction.db_connect import db
from PublicFunction.token import create_token
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash

LoginModule = Blueprint("LoginModule", __name__, template_folder='./templates', static_folder='./static',
                        static_url_path='static')


class Index(MethodView):
    @staticmethod
    def get():
        """
        返回登录页面
        :return:
        """
        return render_template('index.html')

    def post(self):
        return self.get()


class Ver_Inf(MethodView):
    @staticmethod
    def get():
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
        sc = r_code(cd)
        return jsonify(code=cd, msg=sc['inter_ch'], token=o_token)

    def post(self):
        return self.get()


def register_api():
    LoginModule.add_url_rule('/', view_func=Index.as_view('index'), methods=['GET', 'POST'])
    LoginModule.add_url_rule('/ver_inf', view_func=Ver_Inf.as_view('ver_inf'), methods=['GET', 'POST'])


# if __name__ == '__main__':
register_api()
