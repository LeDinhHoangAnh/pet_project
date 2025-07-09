from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.serializers.auth_serializers import RegisterSerializer, LoginSerializer, UserDetailSerializer
from booking.services.auth_services import authenticate_user
from django.conf import settings
import jwt
from datetime import datetime, timedelta

def generate_jwt(user):
    payload = {
        'id': user.id,
        'email': user.user_email,
        'role': user.role.role_name,
        'exp': datetime.utcnow() + timedelta(days=1)
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Đăng ký thành công"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['user_email']
            password = serializer.validated_data['password']
            user = authenticate_user(email, password)
            if user:
                token = generate_jwt(user)
                return Response({
                    "token": token,
                    "role": user.role.role_name,
                    "user": UserDetailSerializer(user).data
                })
            return Response({"error": "Sai email hoặc mật khẩu"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
