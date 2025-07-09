# booking/serializers/showtime_serializer.py
from rest_framework import serializers
from booking.models.showtimes import Showtimes
from booking.models.rooms import Rooms

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ['id', 'room_name']

class ShowtimeSerializer(serializers.ModelSerializer):
    room = RoomSerializer()

    class Meta:
        model = Showtimes
        fields = ['id', 'start_time', 'base_price', 'room']
