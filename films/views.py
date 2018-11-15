from django.views import generic
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect
from django.views.generic.base import TemplateResponseMixin
from .models import Film, Role_Film, Acteur

class Index(generic.ListView):
    model = Film
    template_name = 'film/index.html'
    context_object_name = 'films'
    paginate_by = 10

    def get_queryset(self):
        if self.request.GET.get('query'):
            query  = self.request.GET.get('query')
            queryset = Film.objects.filter(title__icontains=query)
        else:
            queryset = Film.objects.order_by('-created_at')
        return queryset

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
        context['roles_film'] = Role_Film.objects.filter(film_id=pk_URL).order_by('acteur')
        context['suggestions'] = Film.objects.filter(genre_id=film_corrent.genre_id) 
        return context

class DetailActeur(generic.DetailView):
    model = Acteur
    template_name = 'film/detailacteur.html'
    context_object_name = 'acteur'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # recherche de l'ID de film pour accéder au modèle Film/Acteur/Role 
        return context