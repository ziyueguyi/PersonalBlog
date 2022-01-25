from sqlalchemy.orm import backref

from PublicFunction.db_connect import db, BaseTime


class Pro_rout(db.Model, BaseTime):
    __tablename__ = 'pro_rout'
    """目录"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 目录编码
    p_name = db.Column(db.String(80), unique=True, nullable=False)  # 目录名称
    p_url = db.Column(db.String(256), unique=True, nullable=False)  # 目录链接
    p_img_url = db.Column(db.String(256), server_default='default.jpg')  # 目录图片链接
    p_level = db.Column(db.Integer, nullable=False, default=1)  # 目录等级
    superior_id = db.Column(db.Integer, nullable=False, default=1)  # 目录上级id
    sequence = db.Column(db.Integer, default=1, nullable=False)  # 状态
    state = db.Column(db.Boolean, default=True, nullable=False)  # 状态
    flag = db.Column(db.Integer, default=1)  # 链接类型：0>不展示，1>展示，2>后台接口


class Authority_List(db.Model, BaseTime):
    __tablename__ = "authority_list"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    aut_name = db.Column(db.String(255))
    aut_url = db.Column(db.String(256), unique=True, nullable=False)
    add_number = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    aut_state = db.Column(db.Boolean, default=True, nullable=True)


class Authority(db.Model, BaseTime):
    __tablename__ = "authority"
    numbers_u_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True, primary_key=True)
    numbers_al_id = db.Column(db.Integer, db.ForeignKey('authority_list.id'), nullable=False, index=True,
                              primary_key=True)
    add_number = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    user_id = db.relationship('Users', backref=backref('a_u_id', uselist=False), lazy=True,
                              foreign_keys=[numbers_u_id])
    Authority_List_id = db.relationship('Authority_List', backref=backref('a_al_id', uselist=False), lazy=True,
                                        foreign_keys=[numbers_al_id])


class Account_Type(db.Model, BaseTime):
    __tablename__ = 'account_type'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    acc_name = db.Column(db.String(255))
    acc_state = db.Column(db.Boolean, default=True, nullable=True)
    add_number = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
