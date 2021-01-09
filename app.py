from flask import Flask
from LoginModule import LoginModule
from MainModule import MainModule

app = Flask(__name__)
# 注册蓝图模块
app.register_blueprint(LoginModule.LM, url_prefix='/LM')  # 登录模块
app.register_blueprint(MainModule.MM, url_prefix='')  # 主模块


# @app.route('/')
# def hello_world():
#     return 'Hello World!'


@app.route('/favicon.Ico')
def favicon():
    print(__name__)
    return app.send_static_file('/Ico/favicon.Ico')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8888, debug=True)
