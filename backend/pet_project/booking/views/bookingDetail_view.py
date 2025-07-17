from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.models.bookings import Bookings
from booking.views.jwt_auth import jwt_required
from booking.services.bookingDetail_service import get_booking_detail_info
from booking.serializers.bookingDetail_serializer import BookingFullDetailSerializer
class BookingDetailAPIView(APIView):
    @jwt_required
    def get(self, request, booking_id):
        try:
            booking = Bookings.objects.select_related('showtime').get(id=booking_id)
        except Bookings.DoesNotExist:
            return Response({"error": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)

        data = get_booking_detail_info(booking)
        serializer = BookingFullDetailSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
