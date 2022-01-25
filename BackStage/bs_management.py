from flask import Blueprint, render_template, request, jsonify
from flask.views import MethodView
from LoginModule import model as lm_model
from PublicFunction.db_connect import db
from PublicFunction.token import verify_auth_token
from BackStage import model as md
from PublicFunction.public_func import r_code

BackStage = Blueprint("BackStage", __name__, template_folder='./templates', static_folder='./static',
                      static_url_path='static')


class User_Manage(MethodView):

    @staticmethod
    def get():
        """
        用户管理页面
        :return:
        """
        return render_template('pb_index.html')

    def post(self):
        return self.get()


class Resource_Manage(MethodView):
    @staticmethod
    def get():
        """
        资源管理页面
        :return:
        """
        pr_db = md.Pro_rout
        pro_routs = db.session.query(pr_db).filter(pr_db.state == 1 and pr_db.flag == 1).all()
        dir_dic_list = list()
        for pr in pro_routs:
            dir_dic_list.append({
                'id': pr.id,
                'p_name': pr.p_name,
                'p_url': pr.p_url,
                'p_img_url': pr.p_img_url,
                'p_level': pr.p_level,
                'superior_id': pr.superior_id,
                'son': [],
            })
        new__dir_dict = dict()
        for i in range(0, 3):
            for ddl in dir_dic_list:
                if ddl['p_level'] == i:
                    if ddl['p_level'] == 0:
                        new__dir_dict = ddl
                    elif ddl['p_level'] == 1:
                        new__dir_dict['son'].append(ddl)
                    elif ddl['p_level'] == 2:
                        for ndd_son in new__dir_dict['son']:
                            if ndd_son['id'] == ddl['superior_id']:
                                ndd_son['son'].append(ddl)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
        return jsonify(name=new__dir_dict, code=r_code(200))

    def post(self):
        return render_template('resource_manage.html')


class Index(MethodView):
    @staticmethod
    def get():
        """
        后台主页面
        :return:
        """
        return render_template('pb_index.html')

    def post(self):
        return self.get()


class PassWord_Manage(MethodView):
    @staticmethod
    def get():
        """
        用户信息管理页面
        :return:
        """
        return render_template('pb_index.html')

    def post(self):
        return self.get()


class Authority_Manage(MethodView):
    @staticmethod
    def get():
        """
        权限管理页面
        :return:
        """
        return render_template('pb_index.html')

    def post(self):
        return self.get()


class Get_User(MethodView):
    @staticmethod
    def get():
        """
        通过token获取人员信息
        :return:
        """
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

    def post(self):
        return self.get()


def register_api():
    """
    路由注册函数，方便统一管理
    :return:
    """
    BackStage.add_url_rule('/', view_func=Index.as_view('index'), methods=['GET', 'POST'])
    BackStage.add_url_rule('/get_user', view_func=Get_User.as_view('get_user'), methods=['GET', 'POST'])
    BackStage.add_url_rule('/aut_manage', view_func=Authority_Manage.as_view('authority_manage'),
                           methods=['GET', 'POST'])
    BackStage.add_url_rule('/user_manage', view_func=User_Manage.as_view('user_manage'), methods=['GET', 'POST'])
    BackStage.add_url_rule('/pd_manage', view_func=PassWord_Manage.as_view('password_manage'), methods=['GET', 'POST'])
    BackStage.add_url_rule('/res_manage', view_func=Resource_Manage.as_view('resource_manage'), methods=['GET', 'POST'])


# if __name__ == '__main__':
register_api()
