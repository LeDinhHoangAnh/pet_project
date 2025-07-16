from rest_framework import serializers

class BookingCreateSerializer(serializers.Serializer):
    showtime_id = serializers.IntegerField()
    seat_ids = serializers.ListField(child=serializers.IntegerField())
    services = serializers.ListField(
        child=serializers.DictField(child=serializers.IntegerField())
    )
    total_price = serializers.IntegerField()
