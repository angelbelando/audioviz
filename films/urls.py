# Urls de l'aopplication films du site audioviz - nouvelle version
from django.urls import path
from . import views
app_name = 'films'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<pk>', views.DetailFilm.as_view(), name='detail'),
    path('acteur/<int:pk>', views.DetailActeur.as_view(), name='detailacteur'),
]