from django.shortcuts import render
from django.http import JsonResponse
from .models import Country, EyeColor
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(10, cache='default')
def extrafields(request):
    countries = Country.objects.all()
    eyes = EyeColor.objects.all()
    response = {'country': [i.title for i in countries], 'eyes': [i.title for i in eyes]}
    return JsonResponse(response)
