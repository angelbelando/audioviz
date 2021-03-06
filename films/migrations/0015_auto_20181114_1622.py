# Generated by Django 2.1.2 on 2018-11-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0014_auto_20181107_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='photo',
            field=models.ManyToManyField(blank=True, related_name='filmsPhotos', to='films.Photo'),
        ),
        migrations.AlterField(
            model_name='film',
            name='video',
            field=models.ManyToManyField(blank=True, related_name='filmsVideos', to='films.Video'),
        ),
    ]
