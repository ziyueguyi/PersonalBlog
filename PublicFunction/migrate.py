# -*- coding:utf-8 -*-
# @文件名称  :migrate
# @项目名称  :PersonalBlog.py
# @软件名称  :PyCharm
# @创建时间  : 2022-01-14 14:20
# @用户名称  :DELL
from flask_script import Manager
from app import app
from flask_migrate import Migrate, MigrateCommand
from db_connect import db


class Data_Table_Manipulation(object):
    def __init__(self):
        pass

    @staticmethod
    def db_init():
        manager = Manager(app)
        migrate = Migrate(app, db)
        manager.add_command('db', MigrateCommand)
