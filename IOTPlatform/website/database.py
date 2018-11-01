from website import models
from django.db import transaction
from website.utils import create
import time

def login(username, password):
    """
    登录验证
    :param username: 用户名
    :param password: 密码
    :return: {'code': 0, 'message': "", 'data': {'token': token}}
    """
    res = {'code': 0, 'message': "", 'data': {}}
    # 检查参数是否正确
    if not username or not password:
        res['code'] = 1
        res['message'] = 'Parameter error'
        return res
    try:
        # 获取用户对象
        userinfo = models.UserInfo.objects.filter(username=username).first()
        if userinfo:
            if password == userinfo.password:
                # 登陆成功生成token保存并返回（以后每次请求都需携带这个token验证）
                token = create.create_token(username)
                models.UserInfo.objects.filter(username=username).update(token=token)
                res['data']['token'] = token
                return res
            else:
                res['code'] = 1
                res['message'] = 'password error'
                return res
        else:
            res['code'] = 1
            res['message'] = 'user does not exist'
            return res
    except Exception as e:
        res['code'] = 1
        res['message'] = e.__repr__()
        return res


def register(username, password):
    """
    注册用户
    :param username: 用户名（唯一的）
    :param password: 密码
    :return: {'code': 0, 'message': '', 'data': {'user_id': ""}}
    """
    res = {'code': 0, 'message': '', 'data': {}}
    # 检查参数是否正确
    if not username or not password:
        res['code'] = 1
        res['message'] = 'Parameter error'
        return res
    # 检查用户名是否重复
    if models.UserInfo.objects.filter(username=username).first():
        res['code'] = 1
        res['message'] = "repeat username"
        return res
    # 生成user_id
    user_id = hash(username + str(time.time())) % 10 ** 9
    try:
        with transaction.atomic():  # 出错回滚
            models.UserInfo.objects.create(username=username, password=password, user_id=user_id)
            res['message'] = 'Succeed'
            res['data']['user_id'] = user_id
    except Exception as e:
        res['code'] = 1
        res['message'] = e.__repr__()
    return res


