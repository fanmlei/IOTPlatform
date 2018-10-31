from django.db import models

#
# # Create your models here.
#
class UserInfo(models.Model):
    username = models.CharField(max_length=32, null=False)
    user_id = models.IntegerField(unique=True, null=True)
    password = models.CharField(max_length=64, null=False)
