# booking/serializers/showtime_serializer.py
from rest_framework import serializers
from booking.models.showtimes import Showtimes
from booking.models.rooms import Rooms
from booking.models.movies import Movies
from booking.models.rooms import Rooms
from booking.models.movies_genres import MoviesGenres

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ['id', 'room_name']

class ShowtimeSerializer(serializers.ModelSerializer):
    room = RoomSerializer()

    class Meta:
        model = Showtimes
        fields = ['id', 'start_time', 'base_price', 'room']
class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    genre_name = serializers.CharField()

class MovieNestedSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Movies
        fields = ['id', 'title', 'movie_poster_url', 'duration', 'genres']

    def get_genres(self, obj):
        # Lấy danh sách thể loại qua MoviesGenres
        qs = MoviesGenres.objects.filter(movie=obj).select_related('genre')
        return GenreSerializer([mg.genre for mg in qs], many=True).data

class RoomNestedSerializer(serializers.ModelSerializer):
    cinema_name = serializers.CharField(source='cinema.cinemas_name')

    class Meta:
        model = Rooms
        fields = ['room_name', 'room_number', 'cinema_name']

class ShowtimeDetailSerializer(serializers.ModelSerializer):
    movie = MovieNestedSerializer()
    room = RoomNestedSerializer()

    class Meta:
        model = Showtimes
        fields = [
            'id',
            'start_time',
            'base_price',
            'movie',
            'room',
        ]
class ShowtimeItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    start_time = serializers.DateTimeField()
    room_name = serializers.CharField()

class MovieInDateSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField()
    title = serializers.CharField()
    movie_poster_url = serializers.CharField()
    duration = serializers.IntegerField()
    trailer_url = serializers.CharField()
    showtimes = ShowtimeItemSerializer(many=True)

class ShowtimesGroupedByDateSerializer(serializers.Serializer):
    date = serializers.DateField()
    movies = MovieInDateSerializer(many=True)