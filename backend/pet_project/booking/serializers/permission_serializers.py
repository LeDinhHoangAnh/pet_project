from rest_framework import serializers
from booking.models.permissions import Permissions

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = '__all__'
