from django.db import models

#
# # Create your models here.
#
class UserInfo(models.Model):
    username = models.CharField(max_length=32, null=False)
    user_id = models.IntegerField(unique=True, null=True)
    password = models.CharField(max_length=64, null=False)
    sex = models.CharField(max_length=16, null=True)
    birthday = models.CharField(max_length=64, null=True)
    tel = models.CharField(max_length=64, null=True)
    email = models.CharField(max_length=64, null=True)
    address = models.CharField(max_length=64, null=True)
    introduction = models.CharField(max_length=255, null=True)
    token = models.CharField(max_length=255, null=True)