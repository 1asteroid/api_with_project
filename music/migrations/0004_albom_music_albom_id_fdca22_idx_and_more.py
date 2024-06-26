# Generated by Django 5.0.4 on 2024-05-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_albom_options_alter_artist_options_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='albom',
            index=models.Index(fields=['id'], name='music_albom_id_fdca22_idx'),
        ),
        migrations.AddIndex(
            model_name='artist',
            index=models.Index(fields=['id'], name='music_artis_id_a6462a_idx'),
        ),
        migrations.AddIndex(
            model_name='songs',
            index=models.Index(fields=['id'], name='music_songs_id_8977f4_idx'),
        ),
    ]
