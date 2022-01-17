import re
import functools
from config import TestingConfig
from LoginModule.model import Users
from flask import request, g, redirect, url_for, make_response
from PublicFunction.db_connect import db
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature

auth = HTTPBasicAuth()

SECRET_KEY = TestingConfig.SECRET_KEY


def create_token(api_user):
    """
    生成token
    :param api_user:用户id
    :return: token
    """

    # 第一个参数是内部的私钥，这里写在共用的配置信息里了，如果只是测试可以写死
    # 第二个参数是有效期(秒)
    s = Serializer(SECRET_KEY, expires_in=60 * 60 * 12)
    # 接收用户id转换与编码
    token = s.dumps({"id": api_user}).decode("ascii")
    return token


def verify_token(token):
    """
    校验token
    :param token:
    :return: 用户信息 or None
    """
    # 参数为私有秘钥，跟上面方法的秘钥保持一致
    try:
        # 转换为字典
        data = Serializer(SECRET_KEY).loads(token)
        user = Users.query.get(data["id"])
    except Exception as e:
        print(''.format(e))
        return None
    # 拿到转换后的数据，根据模型类去数据库查询用户信息
    return user


def login_required(view_func):
    @functools.wraps(view_func)
    def v_token(*args, **kwargs):
        try:
            # 在请求头上拿到token
            token = request.headers.get('z-token', None)
            Serializer(SECRET_KEY).loads(token)
        except BaseException as e:
            print('{0}token错误'.format(e))
            # 没接收的到token,给前端抛出错误
            # 这里的code推荐写一个文件统一管理。这里为了看着直观就先写死了。
            # return redirect('/LoginModule/index', 302)
            return redirect(url_for('LoginModule'), 302)
        return view_func(*args, **kwargs)
    return v_token


"*************************************"


# 生成token, 有效时间为600min
def generate_auth_token(user_id, expiration=60 * 60 * 12):
    s = Serializer(SECRET_KEY, expires_in=expiration)
    return s.dumps({'user_id': user_id})


# 解析token
def verify_auth_token(token):
    s = Serializer(SECRET_KEY)
    # token正确
    try:
        data = s.loads(token)['id']
        return data
    # token过期
    except BaseException as e:
        ''.format(e)
        return None
    # token错误
    except BadSignature:
        return None


# 验证token
@auth.verify_password
def verify_password(username, password):
    # 先验证token
    user_id = re.sub(r'^"|"$', '', username)
    user_id = verify_auth_token(user_id)
    # 如果token不存在，验证用户id与密码是否匹配
    if not user_id:
        user_id = db.session.query(Users.id).filter(Users.a_name == username,
                                                    Users.password == password).all()
        # 如果用户id与密码对应不上，返回False
        if not user_id:
            return False
    g.user_id = user_id[0][0]
    return True
