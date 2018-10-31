from django.contrib import admin
from django.utils.safestring import mark_safe
# from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType

from .models import Film, Category_Film, Acteur, Role, Role_Film, Video_Type, Video, Photo
# admin.site.register(Film)
class RoleFilmAdmin(admin.TabularInline):
    model = Role_Film

class FilmAdmin(admin.ModelAdmin):
    model = Film
    inlines = [RoleFilmAdmin,]
    list_filter = ['category', 'title']
    list_display = ["title", "category", 'synopsis']
    fields = ["title", "category", 'synopsis', 'picture', 'video', 'photo']

    # readonly_fields = []

admin.site.register(Film, FilmAdmin)

admin.site.register(Category_Film)
admin.site.register(Acteur)
admin.site.register(Role)
# admin.site.register(Role_Film)
admin.site.register(Video_Type)
admin.site.register(Video)
admin.site.register(Photo)
