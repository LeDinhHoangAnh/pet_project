from rest_framework import serializers
from booking.models.admins import Admins

class AdminSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(source='role.role_name', read_only=True)

    class Meta:
        model = Admins
        fields = [
            'id', 'admin_name', 'admin_email', 'admin_password_hash',
            'role', 'role_name', 'created_at'
        ]
        extra_kwargs = {
            'admin_password_hash': {'write_only': True}
        }
