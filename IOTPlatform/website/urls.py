from django.conf.urls import url
from website import views
urlpatterns = [
    url(r'^login$', views.Login.as_view()),  # 登陆验证
    url(r'^register$', views.Register.as_view()),  # 登陆验证
    url(r'^dashboard$', views.Dashboard.as_view()),  # 登陆验证
    url(r'^charts$', views.Chart.as_view()),  # 登陆验证
    url(r'^devices', views.Device.as_view()),  # 登陆验证
    url(r'^streams', views.Stream.as_view()),  # 登陆验证
    url(r'^console', views.Console.as_view()),  # 登陆验证
    url(r'^triggers', views.Trigger.as_view()),  # 登陆验证

]
