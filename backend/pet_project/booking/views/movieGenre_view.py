from rest_framework.views import APIView
from rest_framework.response import Response
from booking.services.movieGenre_service import fetch_genres_for_movie
from booking.serializers.movieGenre_serializer import MovieGenreSerializer
from rest_framework import status

class MovieGenresByMovieAPIView(APIView):
    def get(self, request, movie_id):
        genres = fetch_genres_for_movie(movie_id)
        serializer = MovieGenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
