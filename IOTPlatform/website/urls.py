from django.conf.urls import url
from website import views
urlpatterns = [
    url(r'^login$', views.Login.as_view()),  # 登陆验证
    url(r'^register$', views.Register.as_view()),  # 登陆验证
]