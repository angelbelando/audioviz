from django.db import models
from datetime import date
FILM_STATUS = (
    ('ECO', 'En cours'),
    ('TST', 'Publié Tests'),
    ('PUB', 'Publié'),     
    ('ARC', 'Archivé')
)
DIR_PHOTOS = 'images/Photos/'
DIR_AFFICHES = 'images/AffichesFilms/'
TODAY = date.today()
YEAR = TODAY.year
class Genre_Film(models.Model):
    genre = models.CharField('genre', max_length=32, unique=True)

    class Meta:
        verbose_name = "genre"
    def __str__(self):
        return self.genre

class Acteur(models.Model):
    name = models.CharField('nom', max_length=64, unique=True)
    resumeCV = models.TextField("Résumé CV", blank=True)
    photoActeur = models.ImageField("Photo Acteur", upload_to=DIR_PHOTOS, blank=True)
    class Meta:
        verbose_name = "Acteur"
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField('nom', max_length=64, unique=True)
    description = models.TextField("Description")
    class Meta:
        verbose_name = "Role"
    def __str__(self):
        return self.name

class Video_Type(models.Model):
    name = models.CharField('nom', max_length=40, unique=True)
    def __str__(self):
        return self.name

class Video(models.Model):
    name = models.CharField('nom', max_length=64, unique=True)
    videoType = models.ForeignKey(Video_Type, on_delete=models.CASCADE)
    UrlVideo = models.CharField("URL de la vidéo", max_length=20, blank=True)
    def __str__(self):
        return self.name

class Photo(models.Model):
    name = models.CharField('nom', max_length=60, unique=True)
    photo = models.ImageField("Photo", upload_to=DIR_PHOTOS)
    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField('titre du film', max_length=96, unique=True)
    status = models.CharField(choices=FILM_STATUS, max_length=3, default='ECO')
    genre = models.ForeignKey(Genre_Film, on_delete=models.CASCADE)
    synopsis = models.TextField('synopsis')
    created_at = models.DateTimeField('date de création', auto_now_add=True)
    created_user = models.CharField("utilisateur qui a créé", max_length=32)
    changed_at = models.DateTimeField('date de modification', auto_now_add=True)
    changed_user = models.CharField("utilisateur qui a modifié", max_length=32)
    picture = models.ImageField("Affiche", upload_to=DIR_AFFICHES)
    # acteur = models.ManyToManyField(Acteur, related_name='filmsActeurs', blank=True)
    video = models.ManyToManyField(Video, related_name='filmsVideos', blank=True)
    photo = models.ManyToManyField(Photo, related_name='filmsPhotos', blank=True)
    acteur_role = models.ManyToManyField(Acteur,
        through='Role_Film',
        through_fields=('film', 'acteur', 'role'))
    an_creation = models.IntegerField("Année Création", blank=True, default=YEAR)
    class Meta:
            verbose_name = "film"
    def __str__(self):
        return self.title

class Role_Film(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, default = "")
    acteur = models.ForeignKey(Acteur, on_delete=models.CASCADE, blank=True, default = "")
    roledescription = models.CharField("Role Description", max_length=64, blank=True, default = "")
    class Meta:
        verbose_name = "Rôles des participants dans film"
    def __str__(self):
        return self.roledescription

class Contact(models.Model):
    first_name = models.CharField('Votre prénom', max_length=100)
    name = models.CharField('Votre nom', max_length=100)
    email_address = models.EmailField('Votre adresse email')
    subject = models.CharField('Objet de votre messsage', max_length=100)
    message = models.TextField('Texte de votre message')
    class Meta:
        verbose_name = "Contact"
    def __str__(self):
        return f"{self.first_name} - {self.name}"