from booking.repos.admin_repo import AdminRepository
from django.utils import timezone
import hashlib

class AdminService:
    @staticmethod
    def list_admins():
        return AdminRepository.get_all()

    @staticmethod
    def create_admin(data):
        data['admin_password_hash'] = hashlib.sha256(data['admin_password_hash'].encode()).hexdigest()
        data['created_at'] = timezone.now()
        return AdminRepository.create(data)

    @staticmethod
    def update_admin(admin_id, data):
        admin = AdminRepository.get_by_id(admin_id)
        if not admin:
            return None
        if 'admin_password_hash' in data:
            data['admin_password_hash'] = hashlib.sha256(data['admin_password_hash'].encode()).hexdigest()
        return AdminRepository.update(admin, data)

    @staticmethod
    def delete_admin(admin_id):
        admin = AdminRepository.get_by_id(admin_id)
        if not admin:
            return False
        AdminRepository.delete(admin)
        return True
