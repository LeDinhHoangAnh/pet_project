# booking/views/showtime_view.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.serializers.showtime_serializer import ShowtimeSerializer
from booking.services.showtime_service import ShowtimeService

class ShowtimesByMovie(APIView):
    def get(self, request, movie_id):
        showtimes = ShowtimeService.get_showtimes_by_movie(movie_id)
        serializer = ShowtimeSerializer(showtimes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
