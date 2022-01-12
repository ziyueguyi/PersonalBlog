# -*- coding:utf-8 -*-
# @文件名称  :main
# @项目名称  :数据项目.py
# @软件名称  :PyCharm
# @创建时间  : 2021-10-18 11:36
# @用户名称  :DELL
import config
import pymysql

from gevent import pywsgi
from flask import Flask, render_template
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from BackStage import bs_management
from LoginModule import login
from MainModule import MainModule
from PublicFunction.db_connect import db

pymysql.install_as_MySQLdb()
app = Flask(__name__, template_folder='templates')
manager = Manager(app)
# 注册蓝图模块
app.register_blueprint(login.LoginModule, url_prefix='/LoginModule')  # 登录模块
app.register_blueprint(MainModule.MM, url_prefix='/Main')  # 主模块
app.register_blueprint(bs_management.BackStage, url_prefix='/BackStage')  # 主模块

# mysql连接配置
app.config['SQLALCHEMY_DATABASE_URI'] = config.SDU_TEST
# 指定让SQLAlchemy自动追踪程序修改，会极大消耗内存
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
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


if __name__ == '__main__':
    # manager.run(default_command="runserver")
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), manager)
    server.serve_forever()
