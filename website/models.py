from django.db import models

#
# # Create your models here.
#
class Data(models.Model):
    data = models.CharField(max_length=32)
    date = models.DateTimeField()

class Device(models.Model):
    device_id = models.IntegerField(unique=True, null=False)  # 设备号
    device_name = models.CharField(max_length=32)  # 设备名
    dev_data = models.ManyToManyField(Data)

class UserInfo(models.Model):
    username = models.CharField(max_length=32, null=False)   # 用户名
    user_id = models.IntegerField(unique=True, null=False)   # 用户ID
    password = models.CharField(max_length=64, null=False)   # 密码
    weixin_id = models.CharField(max_length=64, null=True)   # 微信号
    # 个人信息
    sex = models.CharField(max_length=16, null=True)         # 性别
    birthday = models.CharField(max_length=64, null=True)    # 生日
    tel = models.CharField(max_length=64, null=True)         # 联系方式
    email = models.CharField(max_length=64, null=True)       # 邮箱
    address = models.CharField(max_length=64, null=True)     # 地址
    introduction = models.CharField(max_length=255, null=True)   # 个人简介
    token = models.CharField(max_length=255, null=True)

    dev = models.ManyToManyField(Device)




