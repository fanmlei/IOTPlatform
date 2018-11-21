from website import models
from django.db import transaction
from website.utils import create
from utils.time_tools import time_list, day
import time, datetime


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
        res['message'] = '参数有误'
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
                res['code'] = 2
                res['message'] = '密码错误'
                return res
        else:
            res['code'] = 3
            res['message'] = '当前用户不存在'
            return res
    except Exception as e:
        res['code'] = 1
        res['message'] = e.__repr__()
        return res


def register(username, password, email):
    """
    注册用户
    :param username: 用户名（唯一的）
    :param password: 密码
    :param email: 邮箱
    :return: {'code': 0, 'message': '', 'data': {'user_id': ""}}
    """
    res = {'code': 0, 'message': '', 'data': {}}
    # 检查参数是否正确
    if not username or not password or not email:
        res['code'] = 1
        res['message'] = '参数错误'
        return res
    # 检查用户名是否重复
    if models.UserInfo.objects.filter(username=username).first():
        res['code'] = 2
        res['message'] = "用户名已存在"
        return res
    # 生成user_id , user_id是唯一的防止重复
    user_id = hash(username + str(time.time())) % 10 ** 9
    while models.UserInfo.objects.filter(user_id=user_id).first():
        user_id = hash(username + str(time.time())) % 10 ** 9
    try:
        with transaction.atomic():  # 出错回滚
            models.UserInfo.objects.create(username=username, password=password, user_id=user_id, email=email)
            res['message'] = 'Succeed'
            res['data']['user_id'] = user_id
    except Exception as e:
        res['code'] = 3
        res['message'] = e.__repr__()
    return res


def dashboard(username, start_time, end_time):
    res = {'code': 0, 'message': "",
           'data': {
               'card': {"dev_num": 0, "str_num": 0, "dp_num": 0, "trg_num": 0},
               'chart': {'title': [], 'point': []}
           }
           }
    try:
        if not start_time or not end_time:
            end_time = datetime.datetime.now().strftime("%Y-%m-%d")
            start_time = day(end_time, 10)
        date_list = time_list(start_time, end_time)
        date_list.reverse()
        res['data']['chart']['title'] = date_list
        res['data']['chart']['point'] = [0 for i in date_list]

        user_obj = models.UserInfo.objects.filter(username=username).first()
        res['data']['card']['dev_num'] = user_obj.device.count()
        # print(device.first().dev_stream.count())
        for i in user_obj.device.all():
            res['data']['card']['str_num'] += i.dev_stream.count()
            for j in i.dev_stream.all():
                if j.trigger:
                    res['data']['card']['trg_num'] += 1
                res['data']['card']['dp_num'] += j.data.count()
                for t in range(len(date_list)):
                    res['data']['chart']['point'][t] += j.data.filter(date__startswith=date_list[t]).count()
    except Exception as e:
        res['code'] = 1
        res['message'] = e.__repr__()
    return res


def charts(username, start_time, end_time):
    res = {'code': 0, 'message': "", 'data': {}}
    try:

        if not start_time or not end_time:
            end_time = datetime.datetime.now().strftime("%Y-%m-%d")
            start_time = day(end_time, 10)
        date_list = time_list(start_time, end_time)
        date_list.reverse()

        user_obj = models.UserInfo.objects.filter(username=username).first()
        for i in user_obj.device.all():
            res['data'][i.device_name] = {}
            for j in i.dev_stream.all():

                res['data'][i.device_name][j.name] = [[], []]
                for t in j.data.all():
                    res['data'][i.device_name][j.name][0].append(str(t.date)[:19])
                    res['data'][i.device_name][j.name][1].append(t.data)

    except Exception as e:
        res['code'] = 1
        res['message'] = e.__repr__()
    return res


def get_device(username):
    res = {'code': 0, 'message': '', 'data': []}
    try:
        user_obj = models.UserInfo.objects.filter(username=username).first()  # 获取用户对象
        if not user_obj:
            res['code'] = 1
            res['message'] = '无法找到用户信息'
            return res
        for i in user_obj.device.all():  # 遍历其下多有的设备信息
            buff = {'id': i.device_id, 'name': i.device_name, 'status': i.dev_status, 'create_time': str(i.date)[:16],
                    'introduce': i.dev_introduce, 'APIkey': i.apiKey, 'tag': i.tag, 'stream_num': i.dev_stream.count()}
            res['data'].append(buff)

    except Exception as e:
        res['code'] = 1
        res['message'] = e.__repr__()
    return res


def update_device(username, id, name, introduce, tag):
    res = {'code': 0, 'message': "", 'data': {}}
    try:
        # 检查一下此用户下是否存在这个ID 的设备，防止其他人篡改
        dev_obj = models.UserInfo.objects.filter(username=username).device.filter(device_id=id)
        if dev_obj:
            dev_obj.update(device_name=name, tag=tag, dev_introduce=introduce)
        else:
            res['code'] = 1
            res['message'] = '抱歉你的账户下没有这个ID的设备，无法修改'
    except Exception as e:
        res['code'] = 1
        res['message'] = e.__repr__()
    return res


def add_device(username, name, introduce, tag):
    res = {'code': 0, 'message': "", 'data': {}}
    try:
        # 生成唯一的设备ID
        device_id = hash(username + str(time.time())) % 10 ** 9
        while models.Device.objects.filter(device_id=device_id).first():
            device_id = hash(username + str(time.time())) % 10 ** 9
        # 生成设备鉴权信息
        apiKey = create.create_token(str(device_id) + username)
        # 创建设备对象
        dev_obj = models.Device.objects.create(device_id=device_id, device_name=name, dev_introduce=introduce, tag=tag,
                                               apiKey=apiKey)
        # 将创建的设备和用户关联起来
        models.UserInfo.objects.filter(username=username).first().device.add(dev_obj)
    except Exception as e:
        res['code'] = 1
        print(e.__repr__())
        res['message'] = e.__repr__()
    return res


def del_device(username, id, apiKey):
    res = {'code': 0, 'message': "", 'data': {}}
    try:
        # 检查一下此用户下是否存在这个ID 的设备，防止其他人篡改
        dev_obj = models.UserInfo.objects.filter(username=username).first().device.filter(device_id=id)
        if dev_obj:
            # 这里再次判断设备鉴权信息是否正确
            obj = dev_obj.filter(apiKey=apiKey)
            if obj:
                for i in obj.first().dev_stream.all():
                    for d in i.data.all():
                        d.delete()   # 删除数据点
                    i.delete()  # 删除数据流
                obj.delete()  # 这里只是删除了关联，其下的数据流并没有删除， 所以还需要上面的两步删除干净

            else:
                res['code'] = 1
                res['message'] = '设备鉴权信息错误，无法删除'
                return res
        else:
            res['code'] = 1
            res['message'] = '抱歉你的账户下没有这个ID的设备，无法删除'
            return res
    except Exception as e:
        res['code'] = 1
        res['message'] = e.__repr__()
    return res


def get_stream(username):
    res = {'code': 0, 'message': "", 'data': []}
    trigger_type = ['无','<','<=','==','>','>=','change','inout']
    try:
        user_obj = models.UserInfo.objects.filter(username=username).first()
        if not user_obj:
            res['code'] = 1
            res['message'] = '无法找到用户信息'
            return res
        for i in user_obj.device.all():  # 遍历其下多有的设备信息
            for j in i.dev_stream.all():  # 再遍历每个设备下的数据流
                buff = {'name': j.name, 'dev_id': i.device_id, 'dev_name': i.device_name, 'unit': j.unit,
                        'unit_symbol': j.unit_symbol, 'trigger': '是' if j.trigger else '否', 'qos': j.qos, 'max': j.max,
                        'min': j.min, 'trigger_type':trigger_type[j.min]}
                res['data'].append(buff)
    except Exception as e:
        res['code'] = 1
        res['message'] = e.__repr__()
    return res


def update_stream(username, dev_id, name, unit, unit_symbol, max, min, qos):
    res = {'code': 0, 'message': "", 'data': {}}
    try:
        dev_obj = models.UserInfo.objects.filter(username=username).first().device.filter(device_id=dev_id).first()
        if dev_obj:
            dev_obj.dev_stream.filter(name=name).update(unit=unit, unit_symbol=unit_symbol, max=max, min=min, qos=qos)
        else:
            res['code'] = 1
            res['message'] = '抱歉你的账户下没有这个ID的设备，无法修改'
    except Exception as e:
        res['code'] = 1
        res['message'] = e.__repr__()
    return res


def add_stream(username, dev_id, name, unit, unit_symbol, max, min, qos):
    res = {'code': 0, 'message': "", 'data': {}}
    try:
        dev_obj = models.UserInfo.objects.filter(username=username).first().device.filter(device_id=dev_id).first()
        if dev_obj:
            stream_obj = models.DataStream.objects.create(name=name,unit=unit,unit_symbol=unit_symbol,max=max,min=min,qos=qos)
            dev_obj.dev_stream.add(stream_obj)
        else:
            res['code'] = 1
            res['message'] = '抱歉你的账户下没有这个ID的设备，无法新建此数据流'
    except Exception as e:
        res['code'] = 1
        res['message'] = e.__repr__()
    return res


def del_stream(username, dev_id, name):
    res = {'code': 0, 'message': "", 'data': {}}
    try:
        dev_obj = models.UserInfo.objects.filter(username=username).first().device.filter(device_id=dev_id).first()
        if dev_obj:
            str_obj =  dev_obj.dev_stream.filter(name=name)
            for d in str_obj.first().data.all():
                d.delete()   # 删除数据点
            str_obj.delete() # 删除数据流

        else:
            res['code'] = 1
            res['message'] = '抱歉你的账户下没有这个ID的设备，无法删除此数据流'
    except Exception as e:
        res['code'] = 1
        res['message'] = e.__repr__()
    return res


def get_trigger(username):
    res = {'code': 0, 'message': "", 'data': []}
    try:
        user_obj = models.UserInfo.objects.filter(username=username).first()
        if not user_obj:
            res['code'] = 1
            res['message'] = '无法找到用户信息'
            return res
        for i in user_obj.device.all():  # 遍历其下多有的设备信息
            for j in i.dev_stream.all():  # 再遍历每个设备下的数据流
                if j.trigger:
                    buff = {'name': j.name, 'dev_id': i.device_id, 'dev_name': i.device_name, 'unit': j.unit,
                            'unit_symbol': j.unit_symbol, 'trigger': '是' if j.trigger else '否', 'qos': j.qos, 'max': j.max,
                            'min': j.min}
                    res['data'].append(buff)
    except Exception as e:
        res['code'] = 1
        res['message'] = e.__repr__()
    return res
