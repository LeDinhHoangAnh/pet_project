from rest_framework import serializers

class SeatDetailSerializer(serializers.Serializer):
    seat_number = serializers.CharField()
    seat_type = serializers.CharField()
    price = serializers.IntegerField()

class ServiceDetailSerializer(serializers.Serializer):
    service_name = serializers.CharField()
    quantity = serializers.IntegerField()
    unit_price = serializers.IntegerField()
    total_price = serializers.IntegerField()

class BookingFullDetailSerializer(serializers.Serializer):
    seats = SeatDetailSerializer(many=True)
    total_seat_price = serializers.IntegerField()

    services = ServiceDetailSerializer(many=True)
    total_service_price = serializers.IntegerField()

    total_price = serializers.IntegerField()
