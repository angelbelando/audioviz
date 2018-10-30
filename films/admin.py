from django.contrib import admin
from .models import Film, Category_Film, Acteur, Role, Role_Film, Video_Type, Video, Photo
admin.site.register(Film)
admin.site.register(Category_Film)
admin.site.register(Acteur)
admin.site.register(Role)
admin.site.register(Role_Film)
admin.site.register(Video_Type)
admin.site.register(Video)
admin.site.register(Photo)
