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
        films = [
                {"title": "Essai 4", 
                "status": "ECO", 
                "genre": "Documentaire", 
                "synopsis": "test import 4", 
                "created_at": "2018-11-07T07:59:14.338Z", 
                "created_user": "", 
                "changed_at": "2018-11-07T07:59:14.338Z", 
                "changed_user": "", 
                "picture": "Images/AffichesFilms/indisponible.jpg.jpg", 
                "an_creation": 2019, 
                "videos": [{'name':'video_A', 'videoType':'Film_New', 'UrlVideo': '0CeqRg5vzwg'},
                {'name':'video_B', 'videoType':'Film_H', 'UrlVideo': 'KZY4ne1lpco'}
                ],
                "photos": [{'name':'Photo1', 'photo': 'images/AffichesFilms/afficheexperimentalleger.jpg'},
                {'name':'Photo2', 'photo':'images/AffichesFilms/afficheexperimentalleger.jpg'}],
                "acteurs": [{'role':'Acteur', 'acteur':'Jérémy Belando'},
                            {'role':'Acteur', 'acteur':'Benjamin Belando'}]
                },
                {"title": "Essai 2", 
                "status": "ECO", 
                "genre": "Long métrage", 
                "synopsis": "test import 2", 
                "created_at": "2018-11-07T07:59:14.338Z", 
                "created_user": "", 
                "changed_at": "2018-11-07T07:59:14.338Z", 
                "changed_user": "", 
                "picture": "Images/AffichesFilms/Affiche_En_Provence_MGFa0el.jpg", 
                "an_creation": 2019, 
                "videos": [{'name':'', 'videoType':'', 'UrlVideo': ''}],
                "photos": [{'name':'', 'photo': ''}],
                "acteurs": [{'role':'', 'acteur':''}]
                },
                {"title": "Essai 3", 
                "status": "ECO", 
                "genre": "Cuisine", 
                "synopsis": "test import 3", 
                "created_at": "2018-11-07T07:59:14.338Z", 
                "created_user": "", 
                "changed_at": "2018-11-07T07:59:14.338Z", 
                "changed_user": "", 
                "picture": "Images/AffichesFilms/indisponible.jpg", 
                "an_creation": 2019, 
                "videos": [{'name':'video_Z', 'videoType':'Film', 'UrlVideo': '0CeqRg5vzwg'},
                {'name':'video_Y', 'videoType':'Film', 'UrlVideo': 'KZY4ne1lpco'}
                ], 
                "photos": [{'name':'Photo1', 'photo':'images/AffichesFilms/afficheexperimentalleger.jpg'},
                {'name':'Photo2', 'photo':'images/AffichesFilms/afficheexperimentalleger.jpg'}],
                "acteurs": [{'role':'Acteur', 'acteur':'Jérémy Belando'},
                            {'role':'Acteur', 'acteur':'Benjamin Belando'}]
                }
                ]

        # Lire la base myssql et créer la liste films.
   
        cnx = connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='audioviz')
        cursor = cnx.cursor()
        q = 'SELECT title, introtext FROM j34_content where id=194'
        cursor.execute(q)
    
        for t in cursor:
            title = t[0]
            html_doc = t[1]
            # print(f"titre : {title}\n", f"contenu : {html_doc}") 
            soup = BeautifulSoup(html_doc)
            for dd in soup.find_all('dd'):
                print(dd.string)
        cnx.close()

        for film in films:
            obj, new_genre = Genre_Film.objects.get_or_create(
                genre = film['genre']
            )
            try:
                new_film = Film.objects.get(title=film['title'])
                lg.info(f"le film {film['title']} existe dèjà")
            except ObjectDoesNotExist:
                new_film = Film.objects.create(
                title = film['title'],
                status = film['status'],
                genre_id = obj.id,
                synopsis = film['synopsis'],
                created_at = film['created_at'],
                created_user = film['created_user'],
                changed_at = film['changed_at'],
                changed_user = film['changed_user'],
                picture = film['picture'],
                an_creation = film['an_creation'],
                )
                lg.info(f"New Film {film['title']}")
            # Ajouter les vidéos
            if film['videos']:
                videos = film['videos']
            for video in videos:
                obj, new_video_type = Video_Type.objects.get_or_create(
                    name = video['videoType']
                    )
                try:
                    new_video = Video.objects.get(name=video['name'])
                    lg.info(f"la vidéo {video['name']} existe dèjà")  
                except ObjectDoesNotExist:
                    new_video = Video.objects.create(
                    name = video['name'],
                    videoType_id = obj.id,
                    UrlVideo = video['UrlVideo']
                    )
                new_film.video.add(new_video)
            # Ajouter les photos 
            photos = film['photos'] 
            for photo in photos:
                try:
                    new_photo = Photo.objects.get(name=photo['name'])
                    lg.info(f"la photo {photo['name']} existe dèjà")  
                except ObjectDoesNotExist:
                    new_photo = Photo.objects.create(
                    name = photo['name'],
                    photo = photo['photo']
                    )
                new_film.photo.add(new_photo)
            acteurs = film['acteurs']
            for acteur in acteurs:
                try:
                    new_acteur = Acteur.objects.get(name=acteur['acteur'])
                    lg.info(f"l\'acteur {acteur['acteur']} existe dèjà")
                except ObjectDoesNotExist:
                    new_acteur = Acteur.objects.create(
                    name = acteur['acteur'],
                    resumeCV = '',
                    photoActeur = ''                    
                    )
                try:
                    new_role = Role.objects.get(name=acteur['role'])
                    lg.info(f"le role {acteur['role']} existe dèjà")
                except ObjectDoesNotExist:
                    new_role = Role.objects.create(
                    name = acteur['role'],
                    description = acteur['role']                    
                    )
                try:
                    print(new_film.id, new_role.id, new_acteur.id)
                    new_role_film = Role_Film.objects.get(film_id=new_film.id, acteur_id=new_acteur.id, role_id=new_role.id)
                    lg.info(f"le role_Film {acteur['role']}/{acteur['acteur']} existe dèjà")
                except ObjectDoesNotExist:
                    new_role_film = Role_Film.objects.create(
                    acteur_id = new_acteur.id,
                    role_id = new_role.id,
                    film_id = new_film.id,
                    roledescription = ''
                    )