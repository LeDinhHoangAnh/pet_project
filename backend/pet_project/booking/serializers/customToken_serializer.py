from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from booking.models.users import Users

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        email = attrs.get('user_email')
        password = attrs.get('password')

        try:
            user = Users.objects.get(user_email=email)
        except Users.DoesNotExist:
            raise serializers.ValidationError({'detail': 'Email không tồn tại.'})

        if not check_password(password, user.password_hash):
            raise serializers.ValidationError({'detail': 'Mật khẩu không đúng.'})

        # Trick để SimpleJWT hoạt động (phải có username hoặc id để encode token)
        attrs['username'] = email
        self.user = user  # Gán user để dùng trong create_token
        return super().validate(attrs)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.user_email
        token['name'] = user.user_name
        token['role'] = user.role.role_name
        return token
