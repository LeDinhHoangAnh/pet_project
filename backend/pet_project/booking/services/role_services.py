from booking.repos.role_repo import RoleRepository

class RoleService:
    @staticmethod
    def list_roles():
        return RoleRepository.get_all_roles()

    @staticmethod
    def retrieve_role(role_id):
        return RoleRepository.get_role_by_id(role_id)

    @staticmethod
    def create_role(data):
        return RoleRepository.create_role(data)

    @staticmethod
    def update_role(role, data):
        return RoleRepository.update_role(role, data)

    @staticmethod
    def delete_role(role):
        return RoleRepository.delete_role(role)
