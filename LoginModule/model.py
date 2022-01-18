from sqlalchemy.orm import backref
from PublicFunction.db_connect import db, BaseTime


class Users(db.Model, BaseTime):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    a_name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), unique=True, nullable=False)
    uuid = db.Column(db.String(255), default=None, index=True)
    state = db.Column(db.Boolean, default=True, nullable=False)  # 状态
    ui = db.relationship('UserInfo', backref=backref('users_ui', uselist=False), lazy=True)


class UserInfo(db.Model, BaseTime):
    __tablename__ = 'userinfo'
    number = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True, index=True)
    name = db.Column(db.String(80), default='匿名', nullable=False)
    age = db.Column(db.Integer, default=0, nullable=True)
    sex = db.Column(db.Enum('男', '女', '保密'), default='保密')
    phone = db.Column(db.String(11), nullable=True)
    mailbox = db.Column(db.String(256), nullable=True)


class User_Type(db.Model, BaseTime):
    __tablename__ = 'user_type'
    numbers_u_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True, primary_key=True)
    numbers_at_id = db.Column(db.Integer, db.ForeignKey('account_type.id'), nullable=False, index=True, primary_key=True)

    add_number = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)

    user_id = db.relationship('Users', backref=backref('ut_u_id', uselist=False), lazy=True, foreign_keys=[numbers_u_id])
    authority_type_id = db.relationship('Account_Type', backref=backref('tu_at_id', uselist=False), lazy=True,
                                        foreign_keys=[numbers_at_id])
