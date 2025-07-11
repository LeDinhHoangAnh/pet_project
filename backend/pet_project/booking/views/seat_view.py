from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.services.seat_services import get_seat_list_by_showtime, get_seat_status_list_by_showtime
from booking.serializers.seat_serializer import SeatWithStatusSerializer

class SeatByShowtimeView(APIView):
    def get(self, request, showtime_id):
        seat_data = get_seat_list_by_showtime(showtime_id)

        if seat_data is None:
            return Response({'detail': 'Showtime not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response(seat_data, status=status.HTTP_200_OK)

class SeatStatusShowtimeView(APIView):
    def get(self, request, showtime_id):
        data = get_seat_status_list_by_showtime(showtime_id)
        if data is None:
            return Response({'detail': 'Showtime not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SeatWithStatusSerializer(data['seats'], many=True)
        return Response({
            'showtime_id': showtime_id,
            'total': data['total'],
            'seats': serializer.data
        })