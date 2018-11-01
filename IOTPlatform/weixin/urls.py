from django.conf.urls import url
from weixin import views
urlpatterns = [
    url(r'^login$', views.Login.as_view()),  # 登陆验证
]