from rest_framework import serializers
from .models import Artist, Albom, Songs


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("name", "image")   # "__all__" barchasini oladi


class AlbomSerializer(serializers.ModelSerializer):

    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Albom
        fields = ("title", "artist", "cover")


class SongSerializer(serializers.ModelSerializer):

    albom = AlbomSerializer(read_only=True)

    class Meta:
        model = Songs
        fields = ("title", "cover", "albom")