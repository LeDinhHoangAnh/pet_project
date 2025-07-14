from rest_framework import serializers
from booking.models.services import Services

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['id', 'service_name', 'service_description', 'service_price', 'service_image_url']
