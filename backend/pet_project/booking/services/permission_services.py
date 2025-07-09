from booking.repos.permission_repo import PermissionRepository

class PermissionService:
    @staticmethod
    def list_permissions():
        return PermissionRepository.get_all_permissions()

    @staticmethod
    def retrieve_permission(permission_id):
        return PermissionRepository.get_permission_by_id(permission_id)

    @staticmethod
    def create_permission(data):
        return PermissionRepository.create_permission(data)

    @staticmethod
    def update_permission(permission, data):
        return PermissionRepository.update_permission(permission, data)

    @staticmethod
    def delete_permission(permission):
        return PermissionRepository.delete_permission(permission)
