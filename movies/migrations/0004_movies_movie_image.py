# Generated by Django 5.2 on 2025-04-17 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movies_genre_alter_movies_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='movie_image',
            field=models.ImageField(blank=True, null=True, upload_to='movies/images/'),
        ),
    ]
