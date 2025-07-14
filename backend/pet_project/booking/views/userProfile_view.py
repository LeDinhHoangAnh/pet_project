from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from booking.serializers.userProfile_serializer import UserProfileSerializer, UserProfileUpdateSerializer
from booking.services.userProfile_service import UserProfileService
from rest_framework import status, permissions
from booking.services.userProfile_service import UserProfileService
from booking.models.users import Users
from django.db.models import Q

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    # def get(self, request):
    #     serializer = UserProfileSerializer(request.user)
    #     return Response(serializer.data)

    # def put(self, request):
    #     serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        email = request.query_params.get('email')
        if not email:
            return Response({"error": "Missing email"}, status=status.HTTP_400_BAD_REQUEST)

        user = UserProfileService.get_profile_by_email(email)
        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request):
        email = request.data.get('user_email')
        if not email:
            return Response({"error": "Missing email"}, status=status.HTTP_400_BAD_REQUEST)

        user = UserProfileService.get_profile_by_email(email)
        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Kiểm tra trùng tên hoặc số điện thoại (nhưng không tính chính user này)
        name = request.data.get('user_name')
        phone = request.data.get('user_phone')

        if name:
            if Users.objects.filter(user_name=name).exclude(user_email=email).exists():
                return Response({"error": "Tên người dùng đã tồn tại."}, status=status.HTTP_400_BAD_REQUEST)

        if phone:
            if Users.objects.filter(user_phone=phone).exclude(user_email=email).exists():
                return Response({"error": "Số điện thoại đã được sử dụng."}, status=status.HTTP_400_BAD_REQUEST)

        # Tiến hành cập nhật
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        



