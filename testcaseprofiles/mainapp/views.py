from django.shortcuts import render
from django.contrib.auth import get_user_model


def index(request):
    user_model = get_user_model()
    users_info = user_model.objects.all()
    fields = {'eye': 'Цвет глаз',
              'country': 'Страна',
              'email': 'Email',
              'password': 'Хеш пароля',
              'last_name': 'Фамилия',
              'first_name': 'Имя',
              }
    return render(request, 'mainapp/index.html', {"users_info": users_info, 'fields': fields})
