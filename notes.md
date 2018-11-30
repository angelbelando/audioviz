# Notes dévelopement Site WEB Audioviz
### lancer le serveur Django localement
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
.
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
