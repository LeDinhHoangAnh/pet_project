from rest_framework import serializers
from booking.models.role_permissions import RolePermissions, Roles, Permissions

class RolePermissionSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(source='role.role_name', read_only=True)
    permission_name = serializers.CharField(source='permission.permission_name', read_only=True)

    class Meta:
        model = RolePermissions
        fields = ['role', 'permission', 'role_name', 'permission_name']
