# booking/serializers/token_serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'user_email'
