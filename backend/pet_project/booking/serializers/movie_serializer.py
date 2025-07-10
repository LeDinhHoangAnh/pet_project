from rest_framework import serializers
from booking.models.movies import Movies
from booking.serializers.movieGenre_serializer import GenreSerializer
from booking.models.movies_genres import MoviesGenres

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

    def get_genres(self, obj):
        genres = MoviesGenres.objects.filter(movie=obj).select_related('genre')
        return GenreSerializer([mg.genre for mg in genres], many=True).data
