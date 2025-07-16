# booking/views/booking_history_view.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from booking.models.bookings import Bookings
from booking.models.booking_details import BookingDetails
from booking.models.showtimes import Showtimes
from booking.models.movies import Movies
from booking.models.rooms import Rooms
from booking.models.seats import Seats
from booking.models.cinemas import Cinemas
from booking.serializers.bookingHistory_serializer import BookingHistorySerializer
from datetime import date
from booking.views.jwt_auth import jwt_required

class BookingHistoryView(APIView):
    @jwt_required
    def get(self, request):
        user = request.user
        bookings = Bookings.objects.filter(user=user).order_by('-create_at')
        serializer = BookingHistorySerializer(bookings, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)