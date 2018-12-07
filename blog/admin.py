from django.contrib import admin
from django.db import models as django_models
from django_summernote.admin import SummernoteModelAdmin
from .models import Post
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Post, PostAdmin)
