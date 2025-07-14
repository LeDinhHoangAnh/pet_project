from rest_framework import serializers
from booking.models.seat_prices import SeatPrices

class SeatPriceSerializer(serializers.ModelSerializer):
    seat_type_name = serializers.CharField(source='seat_type.seat_type_name', read_only=True)

    class Meta:
        model = SeatPrices
        fields = ['id', 'seat_type', 'seat_type_name', 'price']