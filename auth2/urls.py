from django.conf.urls import *
from django.contrib.auth.views import logout
from auth2 import views

urlpatterns = [
    url(r'register', views.register),
    url(r'login', views.login_func),
    url(r'account_settings', views.account_settings),
    url(r'change_password', views.change_password),
    url(r'change_email', views.change_email),
    url(r'logout', logout, name="logout"),
]
