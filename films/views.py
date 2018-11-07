from django.shortcuts import render
from .models import Film

def index(request):
    films = Film.objects.all()
    context = {
        'films': films}
    return render(request, 'film/index.html', context) 
     
        