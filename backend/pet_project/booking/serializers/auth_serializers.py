from rest_framework import serializers
from booking.repos.user_repo import create_user
from booking.models.users import Users
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.Serializer):
    user_name = serializers.CharField()
    user_email = serializers.EmailField()
    user_phone = serializers.CharField()
    user_address = serializers.CharField(required=False, allow_blank=True)
    password = serializers.CharField(write_only=True, min_length=6)


class LoginSerializer(serializers.Serializer):
    user_email = serializers.EmailField()
    password = serializers.CharField()

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude = ['password_hash']
