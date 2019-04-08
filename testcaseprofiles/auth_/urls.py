from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_, name='logout'),
    path('account/', views.account, name='account'),
    path('', include(('mainapp.urls', 'mainapp'), namespace='main'))
]
