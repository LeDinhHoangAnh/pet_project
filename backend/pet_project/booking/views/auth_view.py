from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.serializers.auth_serializers import RegisterSerializer, LoginSerializer, UserDetailSerializer
from booking.services.auth_services import authenticate_user, create_user
from django.conf import settings
import jwt
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError

def generate_jwt(user):
    payload = {
        'id': user.id,
        'email': user.user_email,
        'user_name': user.user_name, 
        'role': user.role.role_name,
        'exp': datetime.utcnow() + timedelta(days=1)
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    
    # Đảm bảo token là string
    if isinstance(token, bytes):
        token = token.decode('utf-8')
    return token

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = create_user(serializer.validated_data)
                return Response({"message": "Đăng ký thành công!"}, status=status.HTTP_201_CREATED)
            except ValidationError as ve:
                return Response({"error": str(ve)}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"error": "Lỗi không xác định"}, status=status.HTTP_400_BAD_REQUEST)
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
