from django.conf.urls import url
from django.contrib.auth.views import logout
from auth2 import views

urlpatterns = [
    url(r'register', views.register, name="register"),
    url(r'login', views.login_func, name="login"),
    url(r'account_settings', views.account_settings, name="settings"),
    url(r'change_password', views.change_password, name="password"),
    url(r'change_email', views.change_email, name="email"),
    url(r'logout', logout, name="logout"),
]
