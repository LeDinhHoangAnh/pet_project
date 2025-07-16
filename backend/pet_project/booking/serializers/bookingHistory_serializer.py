# booking/serializers/booking_history_serializer.py
from rest_framework import serializers
from datetime import date
from booking.models.bookings import Bookings
from booking.models.booking_details import BookingDetails
from booking.models.showtimes import Showtimes
from booking.models.movies import Movies
from booking.models.rooms import Rooms
from booking.models.seats import Seats
from booking.models.cinemas import Cinemas

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seats
        fields = ['seat_number']

class ShowtimeSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title')
    room_name = serializers.CharField(source='room.room_name')

    class Meta:
        model = Showtimes
        fields = ['movie_title', 'room_name', 'start_time']

class BookingHistorySerializer(serializers.ModelSerializer):
    showtime = ShowtimeSerializer()
    seats = serializers.SerializerMethodField()
    is_new = serializers.SerializerMethodField()

    class Meta:
        model = Bookings
        fields = ['id', 'showtime', 'seats', 'total_price', 'create_at', 'is_new']

    def get_seats(self, obj):
        details = BookingDetails.objects.filter(booking=obj)
        return [d.seat.seat_number for d in details]

    def get_is_new(self, obj):
        return obj.create_at.date() == date.today()
