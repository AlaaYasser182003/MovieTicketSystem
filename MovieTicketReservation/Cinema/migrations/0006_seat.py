# Generated by Django 5.0 on 2023-12-28 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cinema', '0005_reservations'),
    ]

    operations = [
        migrations.CreateModel(
            name='seat',
            fields=[
                ('seatnID', models.AutoField(primary_key=True, serialize=False)),
                ('seatno', models.CharField(max_length=10)),
            ],
        ),
    ]
