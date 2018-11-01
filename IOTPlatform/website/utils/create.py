import hashlib
import time

def create_dev_id(username):
    """
    生成dev_id
    :param username: 用户名
    :return: dev_id
    """
    ctime = str(time.time())
    m = hashlib.md5(bytes(username, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()

def create_token(username):
    """
    生成token，用户登录成功后返回token，下次访问需要携带token验证用户信息
    :param username: 用户名
    :return: token
    """
    ctime = str(time.time())
    m = hashlib.md5(bytes(username, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()