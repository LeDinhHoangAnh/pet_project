from rest_framework import serializers
from booking.models.roles import Roles

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'
