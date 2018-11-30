from django.views import generic
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateResponseMixin
from django.db.models import Count
from .models import Film, Role_Film, Acteur, Genre_Film
from blog.models import Post

class HomeFilms(generic.ListView):
    model = Film
    template_name = 'film/home_films.html'
    context_object_name = 'films'
    paginate_by = 10

    def get_queryset(self):
        if self.request.GET.get('year_search'):
            year_search  = self.request.GET.get('year_search')
        else:
            year_search = 0
        if  self.request.GET.get('genre_search'):
             genre_search  = self.request.GET.get('genre_search')
        else:
            genre_search = "Null"
        if self.request.GET.get('query'):
            query  = self.request.GET.get('query')
        else:
            query = "Null"
        if year_search!=0 and genre_search!="Null" and query!="Null":  
            # requête 1     
            queryset = Film.objects.filter(an_creation=year_search).filter(genre_id=genre_search).filter(title__icontains=query)
        elif year_search!=0 and genre_search!="Null" and query=="Null":
            # requête 2 
            queryset = Film.objects.filter(an_creation=year_search).filter(genre_id=genre_search)
        elif year_search!=0 and genre_search=="Null" and query=="Null":
            # requête 3
            queryset = Film.objects.filter(an_creation=year_search)
        elif year_search!=0 and genre_search=="Null" and query!="Null":
            # requête 4
            queryset = Film.objects.filter(an_creation=year_search).filter(title__icontains=query)
        elif year_search==0 and genre_search!="Null" and query=="Null":
            # requête 5
            queryset = Film.objects.filter(genre_id=genre_search)
        elif year_search==0 and genre_search=="Null" and query!="Null":
            # requête 6
            queryset = Film.objects.filter(title__icontains=query) 
        elif year_search==0 and genre_search!="Null" and query!="Null":   
            queryset = Film.objects.filter(genre_id=genre_search).filter(title__icontains=query)
        else:
            queryset = Film.objects.order_by('-created_at')
        return queryset

    def get_context_data(self, **kwargs):
        if self.request.GET.get('year_search'):
                year_search  = self.request.GET.get('year_search')
        else:
            year_search = 0
        if  self.request.GET.get('genre_search'):
             genre_search  = self.request.GET.get('genre_search')
        else:
            genre_search = "Null"
        if self.request.GET.get('query'):
            query  = self.request.GET.get('query')
        else:
            query = "Null"
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["genres"] = Genre_Film.objects.all()
        context["years"] =  Film.objects.distinct().values('an_creation').order_by('-an_creation')
        context["Filters"] = f"{genre_search}/{year_search}/{query}"
        return context
class Index(generic.ListView):
    model = Film
    template_name = 'film/index.html'
    context_object_name = 'films'
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts']= Post.objects.all().order_by('-post_date')[:3]
        return context
class DetailFilm(generic.DetailView):
    model = Film
    template_name = 'film/detail.html'
    context_object_name = 'film'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # recherche de l'ID de film pour accéder au modèle Film/Acteur/Role
        pk_URL = self.kwargs.get(self.pk_url_kwarg, None)
        film_corrent = Film.objects.get(pk=pk_URL)
        context['roles_film_Autres'] = Role_Film.objects.filter(film_id=pk_URL).order_by('role').exclude(role_id=6)
        context['roles_film_Acteurs'] = Role_Film.objects.filter(film_id=pk_URL).order_by('role').filter(role_id=6)
        context['suggestions'] = Film.objects.filter(genre_id=film_corrent.genre_id) 
        context['ACTEUR'] = 'Acteur'
        return context

class DetailActeur(generic.DetailView):
    model = Acteur
    template_name = 'film/detailacteur.html'
    context_object_name = 'acteur'
    #  query  = self.request.GET.get('query')
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # recherche de l'ID de film pour accéder au modèle Film/Acteur/Role 
        return context