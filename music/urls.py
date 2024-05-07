from django.urls import path, include
from .views import (ArtistAPIViewSet, AlbomAPIViewSet, SongAPIViewSet,
                    ProductAPIViewSet, BasketAPIViewSet, BasketItemsAPIViewSet)
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register("artists", ArtistAPIViewSet)
router.register("alboms", AlbomAPIViewSet)
router.register("songs", SongAPIViewSet)
router.register("products", ProductAPIViewSet)
router.register("basket", BasketAPIViewSet)
router.register("basket-items", BasketItemsAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.obtain_auth_token),
]