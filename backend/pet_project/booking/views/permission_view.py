from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.serializers.permission_serializers import PermissionSerializer
from booking.services.permission_services import PermissionService

class PermissionListCreateView(APIView):
    def get(self, request):
        permissions = PermissionService.list_permissions()
        serializer = PermissionSerializer(permissions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PermissionSerializer(data=request.data)
        if serializer.is_valid():
            permission = PermissionService.create_permission(serializer.validated_data)
            return Response(PermissionSerializer(permission).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PermissionDetailView(APIView):
    def get(self, request, permission_id):
        permission = PermissionService.retrieve_permission(permission_id)
        if permission:
            return Response(PermissionSerializer(permission).data)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, permission_id):
        permission = PermissionService.retrieve_permission(permission_id)
        if not permission:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PermissionSerializer(permission, data=request.data)
        if serializer.is_valid():
            updated = PermissionService.update_permission(permission, serializer.validated_data)
            return Response(PermissionSerializer(updated).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, permission_id):
        permission = PermissionService.retrieve_permission(permission_id)
        if not permission:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        PermissionService.delete_permission(permission)
        return Response(status=status.HTTP_204_NO_CONTENT)
