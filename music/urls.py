from django.urls import path, include
from .views import (ArtistAPIViewSet, AlbomAPIViewSet, SongAPIViewSet)
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register("artists", ArtistAPIViewSet)
router.register("alboms", AlbomAPIViewSet)
router.register("songs", SongAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.obtain_auth_token),
]