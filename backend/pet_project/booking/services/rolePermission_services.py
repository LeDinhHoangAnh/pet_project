from booking.repos.rolePermission_repo import RolePermissionRepository

class RolePermissionService:
    @staticmethod
    def list_role_permissions():
        return RolePermissionRepository.get_all()

    @staticmethod
    def get_permissions_by_role(role_id):
        return RolePermissionRepository.get_by_role(role_id)

    @staticmethod
    def create_role_permission(data):
        return RolePermissionRepository.create(data)

    @staticmethod
    def delete_role_permission(role_permission):
        return RolePermissionRepository.delete(role_permission)
