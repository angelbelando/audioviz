from django.contrib import admin
from django.db import models as django_models
from . import models

admin.site.register(models.Post)
