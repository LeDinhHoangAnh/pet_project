from booking.models.roles import Roles

class RoleRepository:
    @staticmethod
    def get_all_roles():
        return Roles.objects.all()

    @staticmethod
    def get_role_by_id(role_id):
        return Roles.objects.filter(id=role_id).first()

    @staticmethod
    def create_role(data):
        return Roles.objects.create(**data)

    @staticmethod
    def update_role(role, data):
        for attr, value in data.items():
            setattr(role, attr, value)
        role.save()
        return role

    @staticmethod
    def delete_role(role):
        role.delete()
