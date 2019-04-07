from django.urls import path
from . import views

urlpatterns = [
    path('extrafields/', views.extrafields)
]
