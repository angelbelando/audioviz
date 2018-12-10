from django.contrib import admin
from django.utils.safestring import mark_safe
# from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from import_export import resources
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportModelAdmin

from .models import Film, Genre_Film, Acteur, Role, Role_Film, Video_Type, Video, Photo, Contact
# admin.site.register(Film)
class RoleFilmAdmin(admin.TabularInline):
    model = Role_Film

class FilmResource(resources.ModelResource):
    class Meta:
        model = Film
        fields = ('id', 'title', 'genre', 'synopsis','picture')

class FilmAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    summernote_fields = '__all__'
    resource_class = FilmResource
    model = Film
    filter_vertical = ("video","photo",)
    inlines = [RoleFilmAdmin,]
    list_filter = ['genre', 'an_creation']
    list_display = ["title", "genre", 'synopsis']
    fields = ["title", "status", "genre", 'synopsis', 'an_creation', 'picture', 'video', 'photo']

    # readonly_fields = []

admin.site.register(Film, FilmAdmin)

admin.site.register(Genre_Film)
admin.site.register(Acteur)
admin.site.register(Role)
# admin.site.register(Role_Film)
admin.site.register(Video_Type)
admin.site.register(Video)
admin.site.register(Photo)
admin.site.register(Contact)
