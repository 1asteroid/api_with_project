
from .models import Artist, Albom, Songs
from .serializers import ArtistSerializer, AlbomSerializer, SongSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ArtistAPIViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )


class AlbomAPIViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)


class SongAPIViewSet(ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)
