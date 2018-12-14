import os
import logging as lg

from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from films.models import Film, Video, Video_Type, Photo, Genre_Film, Acteur, Role, Role_Film
from mysql import connector
from bs4 import BeautifulSoup
lg.basicConfig(level=lg.DEBUG)


class Command(BaseCommand):
    help = '/'
    
    def handle(self, *args, **options):
        def import_django(photo):
                try:
                    new_photo = Photo.objects.get(name=photo['name'])
                    lg.info(f"la photo {photo['name']} existe dèjà")  
                except ObjectDoesNotExist:
                    new_photo = Photo.objects.create(
                    name = photo['name'],
                    photo = photo['photo']
                    )
   
        cnx = connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='audioviz')
        cursor = cnx.cursor()
        q = 'SELECT imgtitle, imgfilename FROM audioviz.j34_joomgallery'
        cursor.execute(q)
        photo =  {}
        for t in cursor:
            CHEMIN = 'images/Photos/'
            photo['name'] = t[0]
            photo['photo'] = CHEMIN + t[1]
            import_django(photo)
        cnx.close()