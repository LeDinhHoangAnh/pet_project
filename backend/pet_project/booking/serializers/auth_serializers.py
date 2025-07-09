from rest_framework import serializers
from booking.repos.user_repo import create_user
from booking.models.users import Users
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['user_name', 'user_email', 'user_phone', 'user_address', 'password_hash']

    def create(self, validated_data):
        validated_data['password_hash'] = make_password(validated_data['password_hash'])
        return create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    user_email = serializers.EmailField()
    password = serializers.CharField()

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude = ['password_hash']
