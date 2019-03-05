from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateResponseMixin
from django.db.models import Count
from .models import Film, Role_Film, Acteur, Genre_Film
from blog.models import Post
from .forms import ContactForm
from django.core.mail import send_mail, get_connection

class Contact(generic.FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = 'thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        if self.request.recaptcha_is_valid:
            cd = form.cleaned_data
            # envoi message email 
            # con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(cd['subject'], 
            cd['message'],
            cd.get('email', 'relation@audioviz.fr'),
            ['relation@audioviz.fr'],
            # connection=con,
            fail_silently=False
            )
            form.save()
            return super().form_valid(form)
        return render(self.request, 'contact.html', self.get_context_data())

class HomeFilms(generic.ListView):
    model = Film
    template_name = 'film/home_films.html'
    context_object_name = 'films'
    paginate_by = 36
    compteur = 0
    def get_queryset(self):
        if self.request.GET.get('year_search'):
            year_search  = self.request.GET.get('year_search')
        else:
            year_search = 0
        if  self.request.GET.get('genre_search'):
             genre_search  = self.request.GET.get('genre_search')
        else:
            genre_search = "Tous"
        if self.request.GET.get('query'):
            query  = self.request.GET.get('query')
        else:
            query = "Tous"
        if year_search!=0 and genre_search!="Tous" and query!="Tous":  
            # requête 1     
            queryset = Film.objects.filter(an_creation=year_search).filter(genre_id=genre_search).filter(title__icontains=query).filter(status='PUB').order_by('-an_creation')
        elif year_search!=0 and genre_search!="Tous" and query=="Tous":
            # requête 2 
            queryset = Film.objects.filter(an_creation=year_search).filter(genre_id=genre_search).filter(status='PUB').order_by('-an_creation')
        elif year_search!=0 and genre_search=="Tous" and query=="Tous":
            # requête 3
            queryset = Film.objects.filter(an_creation=year_search).filter(status='PUB').order_by('-an_creation')
        elif year_search!=0 and genre_search=="Tous" and query!="Tous":
            # requête 4
            queryset = Film.objects.filter(an_creation=year_search).filter(title__icontains=query).filter(status='PUB').order_by('-an_creation')
        elif year_search==0 and genre_search!="Tous" and query=="Tous":
            # requête 5
            queryset = Film.objects.filter(genre_id=genre_search).filter(status='PUB').order_by('-an_creation')
        elif year_search==0 and genre_search=="Tous" and query!="Tous":
            # requête 6
            queryset = Film.objects.filter(title__icontains=query).filter(status='PUB').order_by('-an_creation')
        elif year_search==0 and genre_search!="Tous" and query!="Tous":   
            queryset = Film.objects.filter(genre_id=genre_search).filter(title__icontains=query).filter(status='PUB').order_by('-an_creation')
        else:
            queryset = Film.objects.order_by('-an_creation').filter(status='PUB')
        compteur = queryset.count() 
        return queryset

    def get_context_data(self, **kwargs):
        if self.request.GET.get('year_search'):
                year_search  = self.request.GET.get('year_search')
        else:
            year_search = 0
        if  self.request.GET.get('genre_search'):
             genre_search  = self.request.GET.get('genre_search')
        else:
            genre_search = "Tous"
        if self.request.GET.get('query'):
            query  = self.request.GET.get('query')
        else:
            query = "Tous"
        if year_search==0 and genre_search=="Tous" and query=="Tous":
            top_filter = False
        else:
            top_filter = True        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["genres"] = Genre_Film.objects.all()
        context["years"] =  Film.objects.distinct().values('an_creation').order_by('-an_creation')
        if year_search == 0:
            year_return = "Toutes"
        else:
            year_return = str(year_search)
        name_genre = "Tous"
        if genre_search != "Tous":
            genre = Genre_Film.objects.get(id=genre_search)
            name_genre = genre.genre
        context["Filters"] = f"Genre: {name_genre} - Année: {year_return} - Titre: {query}"
        context["TopFilter"] = top_filter
        return context
class Index(generic.ListView):
    model = Film
    template_name = 'film/index.html'
    context_object_name = 'films'
    paginate_by = 18
    
    def get_queryset(self):
        queryset = Film.objects.order_by('-an_creation').filter(status='PUB')
        return queryset
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts']= Post.objects.all().order_by('-modified')[:4]
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
        film_current = Film.objects.get(id=pk_URL)
        context['roles_film_Autres'] = Role_Film.objects.filter(film_id=pk_URL).order_by('role').exclude(role_id=1)
        context['roles_film_Acteurs'] = Role_Film.objects.filter(film_id=pk_URL).order_by('role').filter(role_id=1)
        context['suggestions'] = Film.objects.filter(status='PUB').filter(genre_id=film_current.genre_id).order_by('-an_creation')[:4]
        return context

class DetailActeur(generic.DetailView):
    model = Acteur
    template_name = 'film/detailacteur.html'
    context_object_name = 'acteur'
    #  query  = self.request.GET.get('query')
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        pk_URL = self.kwargs.get(self.pk_url_kwarg, None) 
        context['acteur_films'] = Role_Film.objects.filter(acteur_id=pk_URL).distinct('film_id')
        # recherche de l'ID de film pour accéder au modèle Film/Acteur/Role 
        return context