from django.contrib import admin
from django.utils.safestring import mark_safe
# from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from import_export import resources
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportModelAdmin

from .models import Film, Genre_Film, Acteur, Role, Role_Film, Video_Type, Video, Photo, Contact

class RoleFilmAdmin(admin.TabularInline):
    model = Role_Film
    fields = ('role', 'acteur')
    # test

class FilmResource(resources.ModelResource):
    class Meta:
        model = Film
        fields = ('id', 'title', 'genre', 'synopsis','picture')

class FilmAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = '__all__'
    resource_class = FilmResource
    model = Film
    filter_horizontal = ("video","photo",)
    inlines = [RoleFilmAdmin,]
    list_filter = ['genre', 'an_creation', 'status']
    list_display = ["title", "status", "genre", 'synopsis']
    fields = ["title", "status", "genre", 'synopsis', 'picture','an_creation', 'video', 'photo']
    search_fields = ['title',]
    # readonly_fields = []

admin.site.register(Film, FilmAdmin)

admin.site.register(Genre_Film)

class ActeurAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = '__all__'
    search_fields = ['name',]
   

admin.site.register(Acteur, ActeurAdmin)

admin.site.register(Role)
# admin.site.register(Role_Film)
admin.site.register(Video_Type)

class VideoAdmin(admin.ModelAdmin):
    search_fields = ['name',]
admin.site.register(Video, VideoAdmin)

class PhotoAdmin(admin.ModelAdmin):
    search_fields = ['name',]
admin.site.register(Photo, PhotoAdmin) 

admin.site.register(Contact)
