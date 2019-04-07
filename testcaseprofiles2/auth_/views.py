from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django import forms
from .models import User
from django.http import HttpResponseRedirect


class CustomLogin(LoginView):
    template_name = 'auth_/login.html'


class CustomLogout(LogoutView):
    template_name = 'auth_/logout.html'


def login_(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponseRedirect('/')
    return CustomLogin.as_view()(request)


def logout_(request):
    return CustomLogout.as_view()(request)


@login_required()
def account(request):
    class UserForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super(UserForm, self).__init__(*args, **kwargs)
            self.fields['password'].widget.attrs['readonly'] = True

        class Meta:
            model = User
            fields = ['password', 'email', 'eye', 'country', 'last_name', 'first_name']
            labels = {'eye': 'Цвет глаз',
                      'country': 'Страна',
                      'email': 'Email',
                      'password': 'Хеш пароля',
                      'last_name': 'Фамилия',
                      'first_name': 'Имя',
                      }

    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = UserForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/')
    else:
        form = UserForm(instance=user)
        return render(request, 'auth_/account.html', {"form": form})
