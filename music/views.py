
from .models import Artist, Albom, Songs
from .serializers import (ArtistSerializer, AlbomSerializer, SongSerializer,
                          BasketSerializer, BasketItemsSerializer, ProductSerializer)
from product.models import Product
from basket.models import Basket, BasketItems

from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination


class ArtistAPIViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['name']
    pagination_class = LimitOffsetPagination
    # permission_classes = (IsAdminUser, )


class AlbomAPIViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["title", "artist__name"]
    pagination_class = LimitOffsetPagination
    # permission_classes = (IsAdminUser, )


class SongAPIViewSet(ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["$title", "$albom__title", "$albom__artist__name"]
    pagination_class = LimitOffsetPagination
    # permission_classes = (IsAdminUser, )


class ProductAPIViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name", "count", "category"]
    pagination_class = LimitOffsetPagination
    # permission_classes = (IsAdminUser, )


class BasketAPIViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["user__first_name", "user__last_name"]
    pagination_class = LimitOffsetPagination
    # permission_classes = (IsAdminUser, )


class BasketItemsAPIViewSet(ModelViewSet):
    queryset = BasketItems.objects.all()
    serializer_class = BasketItemsSerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["basket__user__first_name", "product_name"]
    pagination_class = LimitOffsetPagination
    # permission_classes = (IsAdminUser, )
