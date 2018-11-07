# Urls de l'aopplication films du site audioviz - nouvelle version

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    # url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^search/$', views.search, name='search'),
]