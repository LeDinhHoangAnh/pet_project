# serializers/seat_serializer.py

from rest_framework import serializers
from booking.models.seats import Seats

class SeatSerializer(serializers.ModelSerializer):
    seat_type_name = serializers.CharField(source='seat_type.seat_type_name')
    seat_status = serializers.CharField(source = 'seat_type.seat_type_status')
    class Meta:
        model = Seats
        fields = ['id', 'seat_number', 'seat_type_name', 'seat_status']

class SeatWithStatusSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    seat_number = serializers.CharField()
    seat_type_name = serializers.CharField()
    status = serializers.CharField()