from django.urls import path, include
from .views import (ArtistAPIViewSet, AlbomAPIViewSet, SongAPIViewSet,
                    ProductAPIViewSet, BasketAPIViewSet, BasketItemsAPIViewSet)
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Music API",
        default_version='v1',
        description="Demo Music API",
        terms_of_service='demo.com',
        contact=openapi.Contact(email='pipsudo@gmail.com'),
        license=openapi.License(name='demo service')
    ),
    public=True,
    permission_classes=(permissions.AllowAny, )
)


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
    path('swagger/', schema_view.with_ui("swagger", cache_timeout=0), name='swagger'),
    path('redoc/', schema_view.with_ui("redoc", cache_timeout=0), name='redoc'),
]
