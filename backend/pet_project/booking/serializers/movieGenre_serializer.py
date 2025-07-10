from rest_framework import serializers
from booking.models.movies_genres import MoviesGenres
from booking.models.genres import Genres

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ['id', 'genre_name']

class MovieGenreSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()

    class Meta:
        model = MoviesGenres
        fields = ['genre']
