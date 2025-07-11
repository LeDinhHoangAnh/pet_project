from rest_framework.response import Response
from booking.serializers.seatPrice_serializer import SeatPriceSerializer
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.services.seatPrice_service import get_prices_for_showtime
from booking.serializers.seatPrice_serializer import SeatPriceSerializer

class SeatPriceView(APIView):
    def get(self, request, showtime_id):
        prices = get_prices_for_showtime(showtime_id)
        serializer = SeatPriceSerializer(prices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
