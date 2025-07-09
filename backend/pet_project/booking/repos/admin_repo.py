from booking.models.admins import Admins

class AdminRepository:
    @staticmethod
    def get_all():
        return Admins.objects.select_related('role').all()

    @staticmethod
    def get_by_id(admin_id):
        return Admins.objects.select_related('role').filter(id=admin_id).first()

    @staticmethod
    def get_by_email(email):
        return Admins.objects.filter(admin_email=email).first()

    @staticmethod
    def create(data):
        return Admins.objects.create(**data)

    @staticmethod
    def update(admin_instance, data):
        for key, value in data.items():
            setattr(admin_instance, key, value)
        admin_instance.save()
        return admin_instance

    @staticmethod
    def delete(admin_instance):
        admin_instance.delete()
