from .base import *

SECRET_KEY = '2oct_bcq26rqqawm%7t9p+tbxnr674@c6#v1$)dr7tzf312c0c'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # on utilise l'adaptateur postgresql
        'NAME': 'BD_Audioviz', # le nom de notre base de donnees creee precedemment
        'USER': 'Angel', # attention : remplacez par votre nom d'utilisateur
        'PASSWORD': 'angel',
        'HOST': '',
        'PORT': '5432',
    }
}