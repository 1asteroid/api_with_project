# Generated by Django 5.0.4 on 2024-05-12 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_songs_listened'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='albom',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='songs',
            options={'ordering': ['id']},
        ),
    ]
