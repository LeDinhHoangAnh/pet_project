from booking.models.permissions import Permissions

class PermissionRepository:
    @staticmethod
    def get_all_permissions():
        return Permissions.objects.all()

    @staticmethod
    def get_permission_by_id(permission_id):
        return Permissions.objects.filter(id=permission_id).first()

    @staticmethod
    def create_permission(data):
        return Permissions.objects.create(**data)

    @staticmethod
    def update_permission(permission, data):
        for attr, value in data.items():
            setattr(permission, attr, value)
        permission.save()
        return permission

    @staticmethod
    def delete_permission(permission):
        permission.delete()
