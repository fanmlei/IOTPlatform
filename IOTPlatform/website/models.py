from django.db import models


class Data(models.Model):
    data = models.CharField(max_length=10)  # 限制在两位小数
    date = models.DateTimeField(auto_now_add=True)  # 上传时间,自动保存时间


class DataStream(models.Model):
    name = models.CharField(max_length=32, null=False)  # 数据流名称
    min = models.IntegerField(null=True, default=0)  # 判断类型  0: None 1: < 2:<= 3:== 4:> 5:>= 6:change 7:inout
    max = models.IntegerField(null=True, default=0)  # 阈值数值
    qos = models.IntegerField(null=True, default=0)  # 服务质量
    unit = models.CharField(max_length=32, null=True)   # 单位名称
    unit_symbol = models.CharField(max_length=32, null=True)   # 单位符号
    trigger = models.BooleanField(default=0)  # 触发器  0:不需要 1:微信 2:邮箱 这两个都是使用userinfo表中绑定的信息  其他http请求（写入的时候需要需要验证URL格式）
    data = models.ManyToManyField(Data)


class Device(models.Model):
    device_id = models.IntegerField(unique=True, null=False)  # 设备号
    device_key = models.CharField(max_length=32, null=True)  # 设备token
    device_name = models.CharField(max_length=32)  # 设备名
    dev_status = models.BooleanField(default=0)  # 在线状态
    dev_introduce = models.TextField(null=True)  # 设备简介
    date = models.DateTimeField(auto_now_add=True)  # 创建时间,自动保存时间
    tag = models.CharField(max_length=32,null=True)  # 设备标签
    apiKey = models.CharField(max_length=32, null=True)  # apiKey
    dev_stream = models.ManyToManyField(DataStream)  # 传感器数据流


class UserInfo(models.Model):
    username = models.CharField(max_length=32, null=False, unique=True, db_index=True)  # 用户名
    user_id = models.IntegerField(unique=True, null=False, db_index=True)  # 用户ID
    password = models.CharField(max_length=64, null=False)  # 密码
    weixin_id = models.CharField(max_length=64, null=True, db_index=True)  # 微信号
    # 个人信息
    sex = models.CharField(max_length=16, null=True)  # 性别
    birthday = models.CharField(max_length=64, null=True)  # 生日
    tel = models.CharField(max_length=64, null=True)  # 联系方式
    email = models.CharField(max_length=64, null=True)  # 邮箱
    address = models.CharField(max_length=64, null=True)  # 地址
    introduction = models.CharField(max_length=255, null=True)  # 个人简介
    token = models.CharField(max_length=255, null=True)
    # 绑定设备
    device = models.ManyToManyField(Device)
