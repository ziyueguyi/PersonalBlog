import os

File_path = os.getcwd()
m_info = {
    "user": "root",
    "password": "hzfdcj",
    "host": "localhost",
    "port": "3306",
    "database": "PersonalBlog",
    'charset': 'utf8mb4',
}

SDU = """mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset={charset}""".format(**m_info)
SDU_TEST = 'sqlite:///' + os.path.join(File_path, 'static/database/PersonalBlog.db').replace('\\', '/')
STATE_CODE = {
    200: {'code': 200, 'msg': '登录成功'},
    4001: {'code': 4001, 'msg': '密码错误'},
    4002: {'code': 4002, 'msg': '账号错误'},
    4003: {'code': 4003, 'msg': '验证码错误'},
    4004: {'code': 4004, 'msg': '验证未通过'},
    4103: {'code': 4103, 'msg': '缺少参数token'},
    4101: {'code': 4101, 'msg': '登录已过期'},
}
SECRET_KEY = "HZFDCJ"
