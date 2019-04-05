# from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView


# todo Разлогинивать, если перешли на /login/ или кидать на главную

class CustomLogin(LoginView):
    template_name = 'auth_/login.html'


class CustomLogout(LogoutView):
    template_name = 'auth_/logout.html'


def login_(request):
    return CustomLogin.as_view()(request)


def logout_(request):
    return CustomLogout.as_view()(request)
