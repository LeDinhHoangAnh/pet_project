from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from booking.serializers.booking_serializer import BookingCreateSerializer
from booking.services.booking_service import BookingService
from booking.views.jwt_auth import jwt_required
class BookingCreateView(APIView):
    @jwt_required
    def post(self, request):
        serializer = BookingCreateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                booking = BookingService.create_booking(request.user, serializer.validated_data)
                return Response({"message": "Đặt vé thành công!", "booking_id": booking.id}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
