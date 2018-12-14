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
        def import_django(film):
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

            videos = film['videos']

            for video in videos:
                if video['name']:
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
            try:
                photos = film['photos'] 
            except:
                photos = []
            for photo in photos:
                if photo['name']:
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
            # print(acteurs)
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
                    # print(new_film.id, new_role.id, new_acteur.id)
                    new_role_film = Role_Film.objects.get(film_id=new_film.id, acteur_id=new_acteur.id, role_id=new_role.id)
                    lg.info(f"le role_Film {acteur['role']}/{acteur['acteur']} existe dèjà")
                except ObjectDoesNotExist:
                    new_role_film = Role_Film.objects.create(
                    acteur_id = new_acteur.id,
                    role_id = new_role.id,
                    film_id = new_film.id,
                    roledescription = ''
                    )

     
        # Lire la base myssql et créer la liste films.
   
        cnx = connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='audioviz')
        cursor = cnx.cursor()
        q = 'SELECT cont.id, cont.title, cont.state, cat.title, cont.introtext, cont.created, cont.modified from audioviz.j34_content as cont inner join audioviz.j34_categories  as cat on cont.catid = cat.id where cont.state = 1 and cat.id = 22 and cont.id > 143'
        cursor.execute(q)
  
        for t in cursor:
            film =  {"title": "", 
                "status": "ECO", 
                "genre": "", 
                "synopsis": "", 
                "created_at": "", 
                "created_user": "", 
                "changed_at": "", 
                "changed_user": "", 
                "picture": "", 
                "an_creation": 0, 
                "videos": [{'name':'', 'videoType':'', 'UrlVideo': ''}],
                "photos": [{'name':'', 'photo': ''}],
                "acteurs": [{'role':'', 'acteur':''}]
                }   

            html_doc = t[4].replace('[','<')
            html_doc = html_doc.replace(']', '>')
            # print(f"titre : {title}\n", f"contenu : {html_doc}") 
            soup = BeautifulSoup(html_doc)
           
            # Recherche affiche à partir de la balise img  
            try: 
                img = soup.find('img')['src']
            except:
                img = 'images/AffichesFilms/indisponible.jpg'
            # print(img)
            i = 0
            # Recherche lien youtube
            for youtube in soup.find_all('youtube'):
                # try:
                i += 1
                film['videos'].append({'name': t[1] + f'-video-{i}', 'videoType': 'Film', 'UrlVideo' : youtube.string })
                # except :
                #     lg.info(f"balise vidéo YOUTUBE non touvée")       
            list_dt = []
            for dt  in soup.find_all('dt'):
                list_dt.append(dt.string) 
            list_dd = []
            for dd  in soup.find_all('dd'):
                list_dd.append(dd.string)
            dt_dd = {x:y for x,y in zip(list_dt, list_dd)}
            # print(dt_dd)
            # affectation synopsis
            try:
                synopsis = dt_dd['Synopsis']
            except:
                synopsis = html_doc

            # affectation acteur
            try:
                acteur1 = dt_dd['Avec'].split('et')
                acteur2 = acteur1[0].split(',')
                acteurs1 = acteur1.pop(0)
                acteurs1 = set(acteur1)
                acteurs2 = set(acteur2)
                acteurs = acteurs1 | acteurs2
                acteurs_final = {x.strip() for x in acteurs}
                # print(acteurs_final)
                film['acteurs'] = []
                for acteur in acteurs_final:
                    film['acteurs'].append({'role': 'Acteur', 'acteur': acteur})
            except:
                film['acteurs'] = []
            #chargement autres roles
          
            for key in dt_dd:
                if key not in ["Synopsis", "Avec"]:
                    film['acteurs'].append({'role': key, 'acteur': dt_dd[key]})
            #chargement des dictionnaires du film  
            # print(film['acteurs'])
            film['title'] = t[1]
            if t[2] == 1:
                film['status'] = 'PUB'
            else:
                film['status'] = 'ECO'
            film['genre'] = t[3]
            film['synopsis'] = synopsis
            film['created_at'] = str(t[5])
            film['created_user'] = 'admin'
            film['changed_at'] = str(t[6])
            film['changed_user'] = 'admin'
            film['picture'] = img
            film['an_creation'] = str(t[5])[0:4]
            # try:
            # except:
            #     lg.info(f"Ajout photos impossible") 
            # print(film)
      
            #import DJANGO
            import_django(film)
        cnx.close()