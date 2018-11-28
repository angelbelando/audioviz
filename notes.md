# Notes dévelopement Site WEB Audioviz
## Se connecter à HEROKU
$ heroku login
### Pousser le dépôt GIT sur HEROKU 
$ git push heroku master
### Dump données de la base de donnée FILMS
$ ./manage.py dumpdata films > films/dumps/films.json
### Importer la base de donnée dans HEROKU
$ heroku run python manage.py loaddata films/dumps/films.json