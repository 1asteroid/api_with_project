from rest_framework import serializers
from .models import Artist, Albom, Songs
from basket.models import BasketItems, Basket
from product.models import Product


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


# Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "description", 'price', "count", "category")


# Basket

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ('user', 'create_date')


class BasketItemsSerializer(serializers.ModelSerializer):

    basket = BasketSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = BasketItems
        fields = ('basket', "product", "quantity")
