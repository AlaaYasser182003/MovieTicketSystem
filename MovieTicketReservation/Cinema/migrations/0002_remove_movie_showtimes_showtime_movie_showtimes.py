# Generated by Django 5.0 on 2023-12-27 18:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cinema', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='showtimes',
        ),
        migrations.AddField(
            model_name='showtime',
            name='movie_showtimes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie_show', to='Cinema.movie'),
        ),
    ]