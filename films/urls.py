# Urls de l'aopplication films du site audioviz - nouvelle version

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]