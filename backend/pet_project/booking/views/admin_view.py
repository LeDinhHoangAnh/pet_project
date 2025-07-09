from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.serializers.admin_serializers import AdminSerializer
from booking.services.admin_services import AdminService

class AdminListCreateView(APIView):
    def get(self, request):
        admins = AdminService.list_admins()
        serializer = AdminSerializer(admins, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            new_admin = AdminService.create_admin(serializer.validated_data)
            return Response(AdminSerializer(new_admin).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminUpdateDeleteView(APIView):
    def put(self, request, admin_id):
        serializer = AdminSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            updated = AdminService.update_admin(admin_id, serializer.validated_data)
            if updated:
                return Response(AdminSerializer(updated).data)
            return Response({'error': 'Admin không tồn tại'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, admin_id):
        success = AdminService.delete_admin(admin_id)
        if success:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Admin không tồn tại'}, status=status.HTTP_404_NOT_FOUND)
