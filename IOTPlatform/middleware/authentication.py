from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, HttpResponse, redirect
from website.datebase import API


class AuthMiddleware(MiddlewareMixin):
    '''
    用户登录验证中间件
    '''
    def process_request(self, request):
        print(request.COOKIES.get('is_log', None))
        print(request.COOKIES.get('username', None))
        print(request.path)
        # print(API().get_user_aid(request.COOKIES.get('username')))
        if request.path != '/oa/login':
            # 如果不是登录页面并且没有登录状态则跳转到登录界面
            if request.COOKIES.get('is_log', None):
                name = request.COOKIES.get('username',None)
                if name:
                    # 获取权限列表中的url
                    url = API().get_user_url(name)
                    url.append('/oa/error')
                    url.append('/oa/userapi')
                    url.append('/oa/api')
                    url.append('/oa/device')
                    url.append('/oa/logout')
                    url.append('/oa/login')
                    url.append('/oa/input/')
                    if url:
                        if request.path in url:
                            return
                        else:
                            return render(request, '../templates/website/bad_request.html')
            else:
                return redirect('/oa/login')
        else:
            return

    def process_view(self, request, callback, callback_args, callback_kwargs):
        pass

    def process_response(self, request):
        pass

    def process_exception(self, request, exception):
        pass

    def process_response(self, request, response):
        return response

