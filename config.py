import os

# 项目基础路径
File_path = os.getcwd()
# 正式数据库
m_info = {
    "user": "root",
    "password": "localhost",
    "host": "localhost",
    "port": "3306",
    "database": "PersonalBlog",
    'charset': 'utf8mb4',
}

# SDU_form = """mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset={charset}""".format(**m_info)  # 正式数据库
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(File_path, 'static/database/PersonalBlog.db').replace('\\',
#                                                                                                             '/')  # 测试数据库
"""
返回状态及说明
"""
STATE_CODE = {
    200: {'code': 200, 'msg': '登录成功'},
    4002: {'code': 4002, 'msg': '账号密码错误'},
    4003: {'code': 4003, 'msg': '验证码错误'},
    4004: {'code': 4004, 'msg': '验证未通过'},
    4103: {'code': 4103, 'msg': '缺少参数token'},
    4101: {'code': 4101, 'msg': '登录已过期'},
}

Ignore_List = [
    '/',
    '/LoginModule',
    '/BackStage',
    '/LoginModule/ver_inf',
]


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 指定让SQLAlchemy自动追踪程序修改，会极大消耗内存
    # PREFERRED_URL_SCHEME = 'https',  # 生成URL的时候如果没有可用的 URL 模式话将使用这个值
    # PROPAGATE_EXCEPTIONS = None,  # 异常传播(是否在控制台打印LOG) 当Debug或者testing开启后,自动为True
    # PRESERVE_CONTEXT_ON_EXCEPTION = None,  # 一两句话说不清楚,一般不用它
    # PERMANENT_SESSION_LIFETIME = 31,  # days , Session的生命周期(天)默认31天
    # USE_X_SENDFILE = False,  # 是否弃用 x_sendfile
    # LOGGER_NAME = None,  # 日志记录器的名称
    # LOGGER_HANDLER_POLICY = 'always',
    # SERVER_NAME = 'example.com',  # 服务访问域名
    # APPLICATION_ROOT = None,  # 项目的完整路径
    # SESSION_COOKIE_NAME = 'session',  # 在cookies中存放session加密字符串的名字
    # SESSION_COOKIE_DOMAIN = None,  # 在哪个域名下会产生session记录在cookies中
    # SESSION_COOKIE_PATH = None,  # cookies的路径
    # SESSION_COOKIE_HTTPONLY = True,  # 控制 cookie 是否应被设置 httponly 的标志，
    # SESSION_COOKIE_SECURE = False,  # 控制 cookie 是否应被设置安全标志
    # SESSION_REFRESH_EACH_REQUEST = True,  # 这个标志控制永久会话如何刷新
    # MAX_CONTENT_LENGTH = None,  # 如果设置为字节数， Flask 会拒绝内容长度大于此值的请求进入，并返回一个 413 状态码
    # END_FILE_MAX_AGE_DEFAULT = 12,  # hours 默认缓存控制的最大期限
    # TRAP_BAD_REQUEST_ERRORS = False,
    # # 如果这个值被设置为 True ，Flask不会执行 HTTP 异常的错误处理，而是像对待其它异常一样，
    # # 通过异常栈让它冒泡地抛出。这对于需要找出 HTTP 异常源头的可怕调试情形是有用的。
    # TRAP_HTTP_EXCEPTIONS = False,
    # # Werkzeug 处理请求中的特定数据的内部数据结构会抛出同样也是“错误的请求”异常的特殊的 key errors 。
    # # 同样地，为了保持一致，许多操作可以显式地抛出 BadRequest 异常。
    # # 因为在调试中，你希望准确地找出异常的原因，这个设置用于在这些情形下调试。
    # # 如果这个值被设置为 True ，你只会得到常规的回溯。
    EXPLAIN_TEMPLATE_LOADING = True,  # 打印加载路径，方便加载
    # JSON_AS_ASCII = True,
    # # 默认情况下 Flask 使用 ascii 编码来序列化对象。如果这个值被设置为 False ，
    # # Flask不会将其编码为 ASCII，并且按原样输出，返回它的 unicode 字符串。
    # # 比如 jsonfiy 会自动地采用 utf-8 来编码它然后才进行传输。
    # JSON_SORT_KEYS = True,
    # # 默认情况下 Flask 按照 JSON 对象的键的顺序来序来序列化它。
    # # 这样做是为了确保键的顺序不会受到字典的哈希种子的影响，从而返回的值每次都是一致的，不会造成无用的额外 HTTP 缓存。
    # # 你可以通过修改这个配置的值来覆盖默认的操作。但这是不被推荐的做法因为这个默认的行为可能会给你在性能的代价上带来改善。
    # JSONIFY_PRETTYPRINT_REGULAR = True,
    # JSONIFY_MIMETYPE = 'application/json',
    # TEMPLATES_AUTO_RELOAD = True,  # 模板更新是否自动加载


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "epsRcwgNwsbFpcMOWBDLccbQIHVeReaSEtSylOlYVXDPRPRpUzDOCOqIKMpzLzKG"  # token秘钥
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(File_path, 'static/database/PersonalBlog.db').replace('\\',
                                                                                                                '/')  # 测试数据库


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SECRET_KEY = "BZbZzuqy"  # token秘钥
    SQLALCHEMY_DATABASE_URI = """mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset={charset}""".format(
        **m_info)  # 正式数据库
