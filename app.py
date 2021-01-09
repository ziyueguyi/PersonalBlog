from flask import Flask

import config
from Modeles.LoginModule import LoginModule
from Modeles.MainModule import MainModule
from PublicFunction.db_connect import db
import pymysql

pymysql.install_as_MySQLdb()
app = Flask(__name__)

# 注册蓝图模块
app.register_blueprint(LoginModule.LM, url_prefix='/LM')  # 登录模块
app.register_blueprint(MainModule.MM, url_prefix='/Main')  # 主模块

# mysql连接配置
app.config['SQLALCHEMY_DATABASE_URI'] = config.SDU
# 指定让SQLAlchemy自动追踪程序修改，会极大消耗内存
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
db.create_all(app=app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/favicon.Ico')
def favicon():
    return app.send_static_file('/Ico/favicon.Ico')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8888, debug=True)
