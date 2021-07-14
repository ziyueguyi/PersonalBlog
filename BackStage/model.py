from PublicFunction.db_connect import db
from datetime import datetime


class Pro_rout(db.Model):
    __tablename__ = 'pro_rout'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    p_name = db.Column(db.String(80), unique=True, nullable=False)
    p_url = db.Column(db.String(256), unique=True, nullable=False)
    p_level = db.Column(db.Integer, nullable=False, default=1)
    superior_id = db.Column(db.Integer, nullable=False, default=1)
    state = db.Column(db.Boolean, default=True, nullable=False)
    create_dt = db.Column(db.DATETIME, default=datetime.now())
    update_dt = db.Column(db.DATETIME, default=datetime.now(), onupdate=datetime.now)
