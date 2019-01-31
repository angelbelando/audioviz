# Notes dévelopement Site WEB Audioviz

## lancer le serveur Django localement

./manage.py runserver

## Se connecter à HEROKU

$ heroku login

### Pousser le dépôt GIT sur HEROKU 

$ git push heroku master

### Dump données de la base de donnée FILMS

$ ./manage.py dumpdata films > films/dumps/films.json

### Importer la base de donnée dans HEROKU

$ heroku run python manage.py migrate
$ heroku run python manage.py loaddata films/dumps/films.json

## Création application BLOG

$ ./manage.py startapp blog

### Rajouter l'application dans setting.py du site audioviz

Modifier le blog INSTALLED_APPS du fichier audioviz/setting.py

### Créer le fichier urls.py de l'application BLOG

..:

### inclure le fichier urls.py de BLOG dans urls.py du site 

path('blog/', include('blog.urls')), 

### Créer le modèle de l'application 

Modifier le fichier blog/model.py

### créer la base de donnée à l'aide de l'outil DJANGO Migrations

$ ./manage.py makemigrations
$ ./manage.py migrate

### Créer le fichier d'aministration du modèles 

Modifier le fichier blog/admin.py

### Créer les fichiers et les templates associer

Modifier les fichiers blog/views et blog/templates
## Boostrap 4.0 avec Django Crispy

[CRISPY](https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html)

## Activer l'environnement (console)  virtuel PIPENV 

$ pipenv shell

## Installation django import/export 

$ pipenv install django-import-export

## Installation Richtext editor Summernote 

$ pipenv install django-summernote

## Parser HTML 

$ pip install BeautifulSoup

## Connecteur MYSQL 

## creation d'un nouveau projet DJANGO

django-admin startproject VanEsthetique

## création d'une clé secrète

```python
import random, string

"".join([random.choice(string.printable) for _ in range(24)])
```

## Installation du module jet pour administrer le site django
[Suivre documentation de jet](https://jet.readthedocs.io/en/latest/)

## Attention aux nomx des répertoires


il faut éviter les mauscules car linux est **case sensitive** mais pas windows
exemple : /media/images/photos

## lancer Psql en ligne de commande 

```bash
psql -d bd_audioviz
bd_audioviz=> 
```
```sql
SELECT * FROM films_film;
```
## Création load Banlancer pour gestion https  

[Digital OCEAN - Load Balancer](https://www.digitalocean.com/docs/networking/load-balancers/how-to/lets-encrypt/)

## Certificat avec NGINX 
[Cerbot](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04)
Please choose whether or not to redirect HTTP traffic to HTTPS, removing HTTP access.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1: No redirect - Make no further changes to the webserver configuration.
2: Redirect - Make all requests redirect to secure HTTPS access. Choose this for
new sites, or if you're confident your site works on HTTPS. You can undo this
change by editing your web server's configuration.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Select the appropriate number [1-2] then [enter] (press 'c' to cancel): 2
Redirecting all traffic on port 80 to ssl in /etc/nginx/sites-enabled/default

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Congratulations! You have successfully enabled https://angel-belando.fr

You should test your configuration at:
https://www.ssllabs.com/ssltest/analyze.html?d=angel-belando.fr
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/angel-belando.fr/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/angel-belando.fr/privkey.pem
   Your cert will expire on 2019-04-23. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot again
   with the "certonly" option. To non-interactively renew *all* of
   your certificates, run "certbot renew"
 - If you like Certbot, please consider supporting our work by
   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le

## Reprise des films audioviz
