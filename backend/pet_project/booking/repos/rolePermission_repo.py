from booking.models.role_permissions import RolePermissions

class RolePermissionRepository:
    @staticmethod
    def get_all():
        return RolePermissions.objects.select_related('role', 'permission').all()

    @staticmethod
    def get_by_role(role_id):
        return RolePermissions.objects.filter(role_id=role_id)

    @staticmethod
    def create(data):
        return RolePermissions.objects.create(**data)

    @staticmethod
    def delete(role_permission):
        role_permission.delete()
