from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from website import models


class Authtication(BaseAuthentication):
    def authenticate(self, request):  # 如果执行到最后一个还是没有给user赋值，则会返回一个匿名用户
        token = request._request.META.get('HTTP_AUTHORIZATION')
        obj = models.UserInfo.objects.filter(token=token).first()
        if not token or not obj:
            raise exceptions.AuthenticationFailed({'code': 1, 'message': '没有登录！', 'data': {}})
        return obj.username, None

