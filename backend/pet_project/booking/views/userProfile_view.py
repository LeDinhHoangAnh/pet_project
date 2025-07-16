from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from booking.serializers.userProfile_serializer import UserProfileSerializer, UserProfileUpdateSerializer
from booking.services.userProfile_service import UserProfileService
from rest_framework import status, permissions
from booking.services.userProfile_service import UserProfileService
from booking.models.users import Users
from django.db.models import Q
from rest_framework import status
from booking.views.jwt_auth import jwt_required

class UserProfileView(APIView):
    @jwt_required
    def get(self, request):
        user = request.user  # ✅ Đã có từ decorator
        return Response({
            "id": user.id,
            "user_email": user.user_email,
            "user_name": user.user_name,
            "user_phone": user.user_phone,
            "user_address": user.user_address,
        })

    @jwt_required
    def put(self, request):
        user = request.user
        data = request.data

        if 'user_name' in data:
            if Users.objects.exclude(id=user.id).filter(user_name=data['user_name']).exists():
                return Response({'error': 'Tên đã tồn tại'}, status=400)

        if 'user_phone' in data:
            if Users.objects.exclude(id=user.id).filter(user_phone=data['user_phone']).exists():
                return Response({'error': 'SĐT đã tồn tại'}, status=400)

        user.user_name = data.get('user_name', user.user_name)
        user.user_phone = data.get('user_phone', user.user_phone)
        user.user_address = data.get('user_address', user.user_address)
        user.save()

        return Response({"message": "Cập nhật thành công"})



