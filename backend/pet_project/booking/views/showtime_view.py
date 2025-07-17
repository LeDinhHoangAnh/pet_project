# booking/views/showtime_view.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.serializers.showtime_serializer import ShowtimeSerializer, ShowtimesGroupedByDateSerializer
from booking.services.showtime_service import ShowtimeService
from booking.serializers.showtime_detail_serializer import ShowtimeDetailSerializer

class ShowtimesByMovie(APIView):
    def get(self, request, movie_id):
        showtimes = ShowtimeService.get_showtimes_by_movie(movie_id)
        serializer = ShowtimeSerializer(showtimes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ShowtimeDetailAPIView(APIView):

    def get(self, request, showtime_id):
        showtime = ShowtimeService.fetch_showtime_detail(showtime_id)
        if not showtime:
            return Response(
                {'error': 'Suất chiếu không tồn tại'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = ShowtimeDetailSerializer(showtime)
        return Response(serializer.data, status=status.HTTP_200_OK)
class MoviesGroupedByShowDateAPIView(APIView):
  def get(self, request):
        data = ShowtimeService.get_showtimes_by_date()
        serializer = ShowtimesGroupedByDateSerializer(data, many=True)
        return Response(serializer.data)

