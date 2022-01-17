from PublicFunction.db_connect import db, BaseTime


class Pro_rout(db.Model, BaseTime):
    __tablename__ = 'pro_rout'
    """目录"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 目录编码
    p_name = db.Column(db.String(80), unique=True, nullable=False)  # 目录名称
    p_url = db.Column(db.String(256), unique=True, nullable=False)  # 目录链接
    p_level = db.Column(db.Integer, nullable=False, default=1)  # 目录等级
    superior_id = db.Column(db.Integer, nullable=False, default=1)  # 目录上级id
    state = db.Column(db.Boolean, default=True, nullable=False)  # 状态
    flag = db.Column(db.Integer, default=1)  # 链接类型


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
