from PublicFunction.db_connect import db
from datetime import datetime


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    a_name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), unique=True, nullable=False)
    ui = db.relationship('UserInfo', backref='a_id', lazy=True)
    create_dt = db.Column(db.DATETIME, default=datetime.now())
    update_dt = db.Column(db.DATETIME, default=datetime.now(), onupdate=datetime.now)


class UserInfo(db.Model):
    __tablename__ = 'userinfo'
    number = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    name = db.Column(db.String(80), default='匿名', nullable=True)
    age = db.Column(db.Integer, default=0, nullable=True)
    sex = db.Column(db.Enum('男', '女', '保密'), default='保密')
    phone = db.Column(db.String(11), nullable=True)
    mailbox = db.Column(db.String(256), nullable=True)
    us = db.relationship('Users', backref='u_id', lazy=True)
    create_dt = db.Column(db.DATETIME, default=datetime.now())
    update_dt = db.Column(db.DATETIME, default=datetime.now(), onupdate=datetime.now)
