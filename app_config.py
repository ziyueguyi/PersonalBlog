# -*- coding:utf-8 -*-
# @文件名称  :app_config
# @项目名称  :PersonalBlog.py
# @软件名称  :PyCharm
# @创建时间  : 2022-01-15 12:47
# @用户名称  :DELL
from BackStage import bs_management
from LoginModule import login
from MainModule import MainModule


def r_app(app):
    app.register_blueprint(MainModule.MM, url_prefix='/Main')  # 前台主模块
    app.register_blueprint(bs_management.BackStage, url_prefix='/BackStage')  # 后台主模块
    app.register_blueprint(login.LoginModule, url_prefix='/LoginModule')  # 登录模块
