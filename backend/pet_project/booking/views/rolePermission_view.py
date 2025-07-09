from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.services.rolePermission_services import RolePermissionService
from booking.serializers.rolePermission_serializers import RolePermissionSerializer
from booking.models import RolePermissions

class RolePermissionListCreateView(APIView):
    def get(self, request):
        data = RolePermissionService.list_role_permissions()
        serializer = RolePermissionSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RolePermissionSerializer(data=request.data)
        if serializer.is_valid():
            instance = RolePermissionService.create_role_permission(serializer.validated_data)
            return Response(RolePermissionSerializer(instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RolePermissionByRoleView(APIView):
    def get(self, request, role_id):
        data = RolePermissionService.get_permissions_by_role(role_id)
        serializer = RolePermissionSerializer(data, many=True)
        return Response(serializer.data)

class RolePermissionDeleteView(APIView):
    def delete(self, request):
        role_id = request.data.get('role')
        permission_id = request.data.get('permission')

        try:
            rp = RolePermissions.objects.get(role_id=role_id, permission_id=permission_id)
            RolePermissionService.delete_role_permission(rp)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except RolePermissions.DoesNotExist:
            return Response({'error': 'Không tìm thấy quyền theo vai trò.'}, status=status.HTTP_404_NOT_FOUND)
