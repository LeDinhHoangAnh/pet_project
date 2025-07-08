# booking/urls.py

from django.urls import path
from booking.views.movie_view import AdminMovieListCreate, AdminMovieDetail

urlpatterns = [
    path('movies/', AdminMovieListCreate.as_view(), name='admin-movie-list-create'),
    path('movies/<int:pk>/', AdminMovieDetail.as_view(), name='admin-movie-detail'),
]
