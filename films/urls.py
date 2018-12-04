# Urls de l'application films du site audioviz - nouvelle version
from django.urls import path
from django.views.generic import TemplateView
from . import views
app_name = 'films'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('home/', views.HomeFilms.as_view(), name='home_films'),
    path('<pk>', views.DetailFilm.as_view(), name='detail'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('contact/thanks/', TemplateView.as_view(template_name='thanks.html'), name='thanks'),
    path('acteur/<int:pk>', views.DetailActeur.as_view(), name='detailacteur'),
]
