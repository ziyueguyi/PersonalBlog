from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

db = SQLAlchemy()


class BaseTime:
    __abstract__ = True
    create_dt = db.Column(db.DateTime(timezone=True), default=func.now())  # 创建时间
    update_dt = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())  # 更新时间
