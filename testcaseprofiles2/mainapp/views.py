from django.shortcuts import render
from django.contrib.auth import get_user_model


def index(request):
    user_model = get_user_model()
    users_info = user_model.objects.all()
    return render(request, 'mainapp/index.html', {"users_info": users_info})
