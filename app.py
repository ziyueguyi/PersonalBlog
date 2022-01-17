# -*- coding:utf-8 -*-
# @文件名称  :main
# @项目名称  :数据项目.py
# @软件名称  :PyCharm
# @创建时间  : 2021-10-18 11:36
# @用户名称  :DELL
import config
import pymysql

from gevent import pywsgi
from flask import Flask, render_template, redirect, request, jsonify, url_for
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from PublicFunction.db_connect import db
from PublicFunction.token import verify_auth_token
from app_config import r_app

pymysql.install_as_MySQLdb()
app = Flask(__name__, template_folder='templates')
manager = Manager(app)
# 注册蓝图模块
r_app(app)
# mysql连接配置
app.config.from_object(config.TestingConfig)
db.init_app(app)
db.create_all(app=app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@app.route('/')
def hello_world():
    return render_template('main.html')


@app.route('/blog.ico')
def favicon():
    return app.send_static_file('./Ico/favicon.Ico')


@app.before_request
def is_login():
    token = request.headers.get('z-token', None)
    ver_token = verify_auth_token(token)
    path = request.path.rstrip('/')
    if path in config.Ignore_List or ver_token or '.' in path:
        return None
    else:
        return redirect('/LoginModule', 302)


# 参数是错误代码
@app.errorhandler(404)
def error404():
    """
    注意，一定要加参数接收错误信息
    :return:
    """
    # 404 Not Found: The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.
    # return '页面不存在'# 可以返回 三剑客 + 小儿子
    return render_template('error_page.html')


if __name__ == '__main__':
    # manager.run(default_command="runserver")
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), manager)
    server.serve_forever()
