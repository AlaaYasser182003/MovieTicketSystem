# Generated by Django 5.0 on 2023-12-27 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cinema', '0002_remove_movie_showtimes_showtime_movie_showtimes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showtime',
            name='movie_showtimes',
        ),
        migrations.AddField(
            model_name='showtime',
            name='movie_showtimes',
            field=models.ManyToManyField(null=True, related_name='movie_show', to='Cinema.movie'),
        ),
    ]
