from rest_framework import viewsets
from booking.models.movies import Movies
from booking.serializers.movie_serializer import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
