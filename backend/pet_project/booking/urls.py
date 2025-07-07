from django.urls import path, include
from rest_framework.routers import DefaultRouter
from booking.views.movie_view import MovieViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movies')

urlpatterns = [
    path('', include(router.urls)),
]
