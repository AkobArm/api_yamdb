from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TitleViewSet, CategoryViewSet, GenreViewSet

router = DefaultRouter()

app_name = 'api'

router.register(r'titles', TitleViewSet, basename='TitleViewSet')
router.register(r'genres', GenreViewSet, basename='GenreViewSet')
router.register(r'categories', CategoryViewSet, basename='CategoryViewSet')

urlpatterns = [
    path('v1/', include(router.urls)),
]
