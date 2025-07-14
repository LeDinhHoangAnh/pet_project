from rest_framework import serializers
from booking.models.users import Users

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['user_name', 'user_email', 'user_phone', 'user_address']
        read_only_fields = ['user_email']  # Không cho sửa email nếu cần

class UserProfileUpdateSerializer(serializers.Serializer):
    user_name = serializers.CharField(required=True, max_length=100)
    user_email = serializers.EmailField(required=True)
    user_phone = serializers.RegexField(regex=r'^0\d{9}$', required=True)
    user_address = serializers.CharField(required=False, allow_blank=True)
