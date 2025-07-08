from booking.services.movie_service import MovieService
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.serializers.movie_serializer import MovieSerializer

class AdminMovieListCreate(APIView):
    def get(self, request):
        movies = MovieService.list_movies()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            movie = MovieService.create(serializer.validated_data)
            return Response(MovieSerializer(movie).data, status=201)
        return Response(serializer.errors, status=400)


class AdminMovieDetail(APIView):
    def get(self, request, pk):
        movie = MovieService.retrieve(pk)
        return Response(MovieSerializer(movie).data)

    def put(self, request, pk):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            movie = MovieService.update(pk, serializer.validated_data)
            return Response(MovieSerializer(movie).data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        MovieService.delete(pk)
        return Response(status=204)

 
class PublicMovieList(APIView):
     def get(self, request):
        movies = MovieService.list_movies()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
     
class PublicMovieDetail(APIView):
     def get(self, request, pk):
        movie = MovieService.retrieve(pk)
        return Response(MovieSerializer(movie).data)
