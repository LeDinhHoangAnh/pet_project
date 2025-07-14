from booking.repos.userProfile_repo import UserProfileRepo
from rest_framework.exceptions import ValidationError

class UserProfileService:
    @staticmethod
    def get_user(user_id):
        return UserProfileRepo.get_by_id(user_id)

    @staticmethod
    def update_user(user_id, data):
        user = UserProfileRepo.get_by_id(user_id)
        if not user:
            raise ValidationError("User không tồn tại")

        # Check email/phone trùng
        if UserProfileRepo.is_email_taken(data['user_email'], user.id):
            raise ValidationError("Email đã được sử dụng.")
        if UserProfileRepo.is_phone_taken(data['user_phone'], user.id):
            raise ValidationError("Số điện thoại đã được sử dụng.")

        return UserProfileRepo.update_user(user, data)
    
    @staticmethod
    def get_profile_by_email(email):
        return UserProfileRepo.get_user_by_email(email)
