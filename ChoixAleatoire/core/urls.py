from django.urls import path 

from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('home', views.home, name='home'),
    path('connexion', views.connexion, name='connexion'),
]